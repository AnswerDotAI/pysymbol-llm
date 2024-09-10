import importlib
import pkgutil
from astroid import MANAGER, FunctionDef, ClassDef
import argparse


def format_symbol(name, signature, doc, decorators=None, is_method=False):
    params = signature.split('(', 1)[1].rsplit(')', 1)[0] if '(' in signature else ''
    decorator_str = ' '.join(f'@{d}' for d in decorators) + ' ' if decorators else ''
    formatted = f"- `{decorator_str}{name}({params})`\n" if is_method else f"- `{decorator_str}def {name}({params})`\n"    
    if doc:
        doc_lines = doc.strip().split('\n')
        formatted += '    ' + '\n    '.join(doc_lines) + '\n'
    return formatted


def get_public_symbols(module, include_no_docstring):
    symbols = []
    for name, obj in module.items():
        if is_public_symbol(name):
            try:
                if isinstance(obj, FunctionDef):
                    symbol = process_function(obj, name, include_no_docstring)
                    if symbol: symbols.append(symbol)
                elif isinstance(obj, ClassDef):
                    symbols.append(process_class(obj, name, include_no_docstring))
            except Exception as e: log_error(name, e)
    return symbols

def is_public_symbol(name):
    return not name.startswith('_') or (name.startswith('__') and name.endswith('__'))

def process_function(func, name, include_no_docstring):
    params = get_params(func)
    signature = f"{name}({params})"
    doc = func.doc_node.value if func.doc_node else ""
    decorators = get_decorators(func)
    if include_no_docstring or doc:
        return ('function', name, signature, doc, decorators)
    return None

def process_class(cls, name, include_no_docstring):
    class_doc = cls.doc_node.value if cls.doc_node else ""
    class_decorators = get_decorators(cls)
    methods = [process_method(method, method_name) 
               for method_name, method in cls.items() 
               if is_valid_method(method, method_name)]
    return ('class', name, class_doc, class_decorators, methods)

def process_method(method, method_name):
    method_params = get_params(method)
    method_signature = f"{method_name}({method_params})"
    method_doc = method.doc_node.value if method.doc_node else ""
    method_decorators = get_decorators(method)
    return (method_name, method_signature, method_doc, method_decorators)

def is_valid_method(method, method_name):
    return isinstance(method, FunctionDef) and is_public_symbol(method_name)

def get_params(func):
    return ', '.join(arg.name for arg in func.args.args)

def get_decorators(obj):
    return [d.as_string() for d in obj.decorators.nodes] if obj.decorators else []

def log_error(name, error):
    raise RuntimeError(f"Error processing symbol {name}: {str(error)}")

def generate_filelist(package_name, output_file, include_no_docstring):
    with open(output_file, 'w') as f:
        f.write(f"# {package_name} Module Documentation\n\n")
        
        try:
            package = importlib.import_module(package_name)
        except ImportError:
            raise ImportError(f"Could not import package {package_name}. Is it installed?")

        for _, module_name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
            try:
                print(f"Processing module: {module_name}")
                module = MANAGER.ast_from_module_name(module_name)
                symbols = get_public_symbols(module, include_no_docstring)
                
                if symbols:
                    f.write(f"## {module_name}\n\n")
                    
                    # Add module-level docstring
                    module_doc = module.doc_node.value if module.doc_node else ""
                    if module_doc:
                        f.write("> " + "\n> ".join(module_doc.strip().split('\n')) + "\n\n")
                    
                    for symbol in symbols:
                        if symbol[0] == 'function':
                            _, name, signature, doc, decorators = symbol
                            decorator_str = ' '.join(f'@{d}' for d in decorators)
                            f.write(f"- `{decorator_str} def {signature}`\n")
                            if doc:
                                f.write(f"    {doc.strip()}\n\n")
                        elif symbol[0] == 'class':
                            _, name, class_doc, class_decorators, methods = symbol
                            decorator_str = ' '.join(f'@{d}' for d in class_decorators)
                            f.write(f"- `{decorator_str} class {name}`\n")
                            if class_doc:
                                f.write(f"    {class_doc.strip()}\n\n")
                            for method_name, method_signature, method_doc, method_decorators in methods:
                                method_decorator_str = ' '.join(f'@{d}' for d in method_decorators)
                                f.write(f"    - `{method_decorator_str} def {method_signature}`\n")
                                if method_doc:
                                    f.write(f"        {method_doc.strip()}\n\n")
                else:
                    print(f"No public symbols found in {module_name}")
            except Exception as e:
                raise RuntimeError(f"Error processing {module_name}: {str(e)}")

    print(f"Documentation generated in {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate documentation for a Python package")
    parser.add_argument("package_name", help="Name of the package to document")
    parser.add_argument("--output", default="filelist.md", help="Output file name")
    parser.add_argument("--include-no-docstring", action="store_true", help="Include symbols without docstrings")
    args = parser.parse_args()

    generate_filelist(args.package_name, args.output, args.include_no_docstring)