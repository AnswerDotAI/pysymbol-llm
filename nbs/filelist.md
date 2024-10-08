# fastcore Module Documentation

## fastcore.basics

> Basic functionality used in the fastai library

- `def ifnone(a, b)`
    `b` if `a` is None else `a`

- `def maybe_attr(o, attr)`
    `getattr(o,attr,o)`

- `def basic_repr(flds)`
    Minimal `__repr__`

- `def is_array(x)`
    `True` if `x` supports `__array__` or `iloc`

- `def listify(o, *rest)`
    Convert `o` to a `list`

- `def tuplify(o, use_list, match)`
    Make `o` a tuple

- `def true(x)`
    Test whether `x` is truthy; collections with >0 elements are considered `True`

- `class NullType`
    An object that is `False` and can be called, chained, and indexed

    - `def __getattr__(self, *args)`
    - `def __call__(self, *args, **kwargs)`
    - `def __getitem__(self, *args)`
    - `def __bool__(self)`

- `def tonull(x)`
    Convert `None` to `null`

- `def get_class(nm, *fld_names, **flds)`
    Dynamically create a class, optionally inheriting from `sup`, containing `fld_names`

- `def mk_class(nm, *fld_names, **flds)`
    Create a class using `get_class` and add to the caller's module

- `def wrap_class(nm, *fld_names, **flds)`
    Decorator: makes function a method of a new class `nm` passing parameters to `mk_class`

- `class ignore_exceptions`
    Context manager to ignore exceptions

    - `def __enter__(self)`
    - `def __exit__(self, *args)`

- `def exec_local(code, var_name)`
    Call `exec` on `code` and return the var `var_name`

- `def risinstance(types, obj)`
    Curried `isinstance` but with args reversed

- `class Inf`
    Infinite lists


- `def in_(x, a)`
    `True` if `x in a`

- `def ret_true(*args, **kwargs)`
    Predicate: always `True`

- `def ret_false(*args, **kwargs)`
    Predicate: always `False`

- `def stop(e)`
    Raises exception `e` (by default `StopIteration`)

- `def gen(func, seq, cond)`
    Like `(func(o) for o in seq if cond(func(o)))` but handles `StopIteration`

- `def chunked(it, chunk_sz, drop_last, n_chunks)`
    Return batches from iterator `it` of size `chunk_sz` (or return `n_chunks` total)

- `def otherwise(x, tst, y)`
    `y if tst(x) else x`

- `def custom_dir(c, add)`
    Implement custom `__dir__`, adding `add` to `cls`

- `class AttrDict`
    `dict` subclass that also provides access to keys as attrs

    - `def __getattr__(self, k)`
    - `def __setattr__(self, k, v)`
    - `def __dir__(self)`
    - `def copy(self)`

- `class AttrDictDefault`
    `AttrDict` subclass that returns `None` for missing attrs

    - `def __init__(self, *args, **kwargs)`
    - `def __getattr__(self, k)`

- `class NS`
    `SimpleNamespace` subclass that also adds `iter` and `dict` support

    - `def __iter__(self)`
    - `def __getitem__(self, x)`
    - `def __setitem__(self, x, y)`

- `def get_annotations_ex(obj)`
    Backport of py3.10 `get_annotations` that returns globals/locals

- `def eval_type(t, glb, loc)`
    `eval` a type or collection of types, if needed, for annotations in py3.10+

- `def type_hints(f)`
    Like `typing.get_type_hints` but returns `{}` if not allowed type

- `def annotations(o)`
    Annotations for `o`, or `type(o)`

- `def anno_ret(func)`
    Get the return annotation of `func`

- `def signature_ex(obj, eval_str)`
    Backport of `inspect.signature(..., eval_str=True` to <py310

- `def argnames(f, frame)`
    Names of arguments to function or frame `f`

- `def with_cast(f)`
    Decorator which uses any parameter annotations as preprocessing functions

- `def store_attr(names, self, but, cast, store_args, **attrs)`
    Store params named in comma-separated `names` from calling context into attrs in `self`

- `def attrdict(o, *ks)`
    Dict from each `k` in `ks` to `getattr(o,k)`

- `def properties(cls, *ps)`
    Change attrs in `cls` with names in `ps` to properties

- `def camel2words(s, space)`
    Convert CamelCase to 'spaced words'

- `def camel2snake(name)`
    Convert CamelCase to snake_case

- `def snake2camel(s)`
    Convert snake_case to CamelCase

- `def class2attr(self, cls_name)`
    Return the snake-cased name of the class; strip ending `cls_name` if it exists.

- `def getcallable(o, attr)`
    Calls `getattr` with a default of `noop`

- `def getattrs(o, *attrs)`
    List of all `attrs` in `o`

- `def hasattrs(o, attrs)`
    Test whether `o` contains all `attrs`

- `def try_attrs(obj, *attrs)`
    Return first attr that exists in `obj`

- `class GetAttrBase`
    Basic delegation of `__getattr__` and `__dir__`

    - `def __getattr__(self, k)`
    - `def __dir__(self)`

- `class GetAttr`
    Inherit from this to have all attr accesses in `self._xtra` passed down to `self.default`

    - `def __getattr__(self, k)`
    - `def __dir__(self)`
    - `def __setstate__(self, data)`

- `def delegate_attr(self, k, to)`
    Use in `__getattr__` to delegate to attr `to` without inheriting from `GetAttr`

- `class ShowPrint`
    Base class that prints for `show`

    - `def show(self, *args, **kwargs)`

- `class Int`
    An extensible `int`


- `class Str`
    An extensible `str`


- `class Float`
    An extensible `float`


- `def partition(coll, f)`
    Partition a collection by a predicate

- `def flatten(o)`
    Concatenate all collections and items as a generator

- `def concat(colls)`
    Concatenate all collections and items as a list

- `def strcat(its, sep)`
    Concatenate stringified items `its`

- `def detuplify(x)`
    If `x` is a tuple with one thing, extract it

- `def replicate(item, match)`
    Create tuple of `item` copied `len(match)` times

- `def setify(o)`
    Turn any list like-object into a set.

- `def merge(*ds)`
    Merge all dictionaries in `ds`

- `def range_of(x)`
    All indices of collection `x` (i.e. `list(range(len(x)))`)

- `def groupby(x, key, val)`
    Like `itertools.groupby` but doesn't need to be sorted, and isn't lazy, plus some extensions

- `def last_index(x, o)`
    Finds the last index of occurence of `x` in `o` (returns -1 if no occurence)

- `def filter_dict(d, func)`
    Filter a `dict` using `func`, applied to keys and values

- `def filter_keys(d, func)`
    Filter a `dict` using `func`, applied to keys

- `def filter_values(d, func)`
    Filter a `dict` using `func`, applied to values

- `def cycle(o)`
    Like `itertools.cycle` except creates list of `None`s if `o` is empty

- `def zip_cycle(x, *args)`
    Like `itertools.zip_longest` but `cycle`s through elements of all but first argument

- `def sorted_ex(iterable, key, reverse)`
    Like `sorted`, but if key is str use `attrgetter`; if int use `itemgetter`

- `def not_(f)`
    Create new function that negates result of `f`

- `def argwhere(iterable, f, negate, **kwargs)`
    Like `filter_ex`, but return indices for matching items

- `def filter_ex(iterable, f, negate, gen, **kwargs)`
    Like `filter`, but passing `kwargs` to `f`, defaulting `f` to `noop`, and adding `negate` and `gen`

- `def renumerate(iterable, start)`
    Same as `enumerate`, but returns index as 2nd element instead of 1st

- `def first(x, f, negate, **kwargs)`
    First element of `x`, optionally filtered by `f`, or None if missing

- `def only(o)`
    Return the only item of `o`, raise if `o` doesn't have exactly one item

- `def nested_attr(o, attr, default)`
    Same as `getattr`, but if `attr` includes a `.`, then looks inside nested objects

- `def nested_setdefault(o, attr, default)`
    Same as `setdefault`, but if `attr` includes a `.`, then looks inside nested objects

- `def nested_callable(o, attr)`
    Same as `nested_attr` but if not found will return `noop`

- `def nested_idx(coll, *idxs)`
    Index into nested collections, dicts, etc, with `idxs`

- `def set_nested_idx(coll, value, *idxs)`
    Set value indexed like `nested_idx

- `def val2idx(x)`
    Dict from value to index

- `def uniqueify(x, sort, bidir, start)`
    Unique elements in `x`, optional `sort`, optional return reverse correspondence, optional prepend with elements.

- `def loop_first_last(values)`
    Iterate and generate a tuple with a flag for first and last value.

- `def loop_first(values)`
    Iterate and generate a tuple with a flag for first value.

- `def loop_last(values)`
    Iterate and generate a tuple with a flag for last value.

- `def first_match(lst, f, default)`
    First element of `lst` matching predicate `f`, or `default` if none

- `def last_match(lst, f, default)`
    Last element of `lst` matching predicate `f`, or `default` if none

- `class fastuple`
    A `tuple` with elementwise ops and more friendly __init__ behavior

    - `def __new__(cls, x, *rest)`
    - `def mul(self, *args)`
        `*` is already defined in `tuple` for replicating, so use `mul` instead

    - `def add(self, *args)`
        `+` is already defined in `tuple` for concat, so use `add` instead


- `class bind`
    Same as `partial`, except you can use `arg0` `arg1` etc param placeholders

    - `def __init__(self, func, *pargs, **pkwargs)`
    - `def __call__(self, *args, **kwargs)`

- `def mapt(func, *iterables)`
    Tuplified `map`

- `def map_ex(iterable, f, *args, **kwargs)`
    Like `map`, but use `bind`, and supports `str` and indexing

- `def compose(*funcs)`
    Create a function that composes all functions in `funcs`, passing along remaining `*args` and `**kwargs` to all

- `def maps(*args)`
    Like `map`, except funcs are composed first

- `def partialler(f, *args, **kwargs)`
    Like `functools.partial` but also copies over docstring

- `def instantiate(t)`
    Instantiate `t` if it's a type, otherwise do nothing

- `def using_attr(f, attr)`
    Construct a function which applies `f` to the argument's attribute `attr`

- `def copy_func(f)`
    Copy a non-builtin function (NB `copy.copy` does not work for this)

- `def patch_to(cls, as_prop, cls_method)`
    Decorator: add `f` to `cls`

- `def patch(f)`
    Decorator: add `f` to the first parameter's class (based on f's type annotations)

- `def patch_property(f)`
    Deprecated; use `patch(as_prop=True)` instead

- `def compile_re(pat)`
    Compile `pat` if it's not None

- `class ImportEnum`
    An `Enum` that can have its values imported

    - `@classmethod def imports(cls)`
    - `@property def name(self)`

- `class StrEnum`
    An `ImportEnum` that behaves like a `str`

    - `def __str__(self)`
    - `@property def name(self)`

- `def str_enum(name, *vals)`
    Simplified creation of `StrEnum` types

- `class ValEnum`
    An `ImportEnum` that stringifies using values

    - `def __str__(self)`
    - `@property def name(self)`

- `class Stateful`
    A base class/mixin for objects that should not serialize all their state

    - `def __init__(self, *args, **kwargs)`
    - `def __getstate__(self)`
    - `def __setstate__(self, state)`

- `class NotStr`
    Behaves like a `str`, but isn't an instance of one

    - `def __init__(self, s)`
    - `def __repr__(self)`
    - `def __str__(self)`
    - `def __add__(self, b)`
    - `def __mul__(self, b)`
    - `def __len__(self)`
    - `def __eq__(self, b)`
    - `def __lt__(self, b)`
    - `def __hash__(self)`
    - `def __bool__(self)`
    - `def __contains__(self, b)`
    - `def __iter__(self)`

- `class PrettyString`
    Little hack to get strings to show properly in Jupyter.

    - `def __repr__(self)`

- `def even_mults(start, stop, n)`
    Build log-stepped array from `start` to `stop` in `n` steps.

- `def num_cpus()`
    Get number of cpus

- `def add_props(f, g, n)`
    Create properties passing each of `range(n)` to f

- `def typed(f)`
    Decorator to check param and return types at runtime

- `def exec_new(code)`
    Execute `code` in a new environment and return it

- `def exec_import(mod, sym)`
    Import `sym` from `mod` in a new environment

- `def str2bool(s)`
    Case-insensitive convert string `s` too a bool (`y`,`yes`,`t`,`true`,`on`,`1`->`True`)

## fastcore.dispatch

> Basic single and dual parameter dispatch

- `def lenient_issubclass(cls, types)`
    If possible return whether `cls` is a subclass of `types`, otherwise return False.

- `def sorted_topologically(iterable)`
    Return a new list containing all items from the iterable sorted topologically

- `class TypeDispatch`
    Dictionary-like object; `__getitem__` matches keys of types using `issubclass`

    - `def __init__(self, funcs, bases)`
    - `def add(self, f)`
        Add type `t` and function `f`

    - `def first(self)`
        Get first function in ordered dict of type:func.

    - `def returns(self, x)`
        Get the return type of annotation of `x`.

    - `def __repr__(self)`
    - `def __call__(self, *args, **kwargs)`
    - `def __get__(self, inst, owner)`
    - `def __getitem__(self, k)`
        Find first matching type that is a super-class of `k`


- `class DispatchReg`
    A global registry for `TypeDispatch` objects keyed by function name

    - `def __init__(self)`
    - `def __call__(self, f)`

- `def retain_meta(x, res, as_copy)`
    Call `res.set_meta(x)`, if it exists

- `def default_set_meta(self, x, as_copy)`
    Copy over `_meta` from `x` to `res`, if it's missing

- `@typedispatch def cast(x, typ)`
    cast `x` to type `typ` (may also change `x` inplace)

- `def retain_type(new, old, typ, as_copy)`
    Cast `new` to type of `old` or `typ` if it's a superclass

- `def retain_types(new, old, typs)`
    Cast each item of `new` to type of matching item in `old` if it's a superclass

- `def explode_types(o)`
    Return the type of `o`, potentially in nested dictionaries for thing that are listy

## fastcore.docments

> Document parameters using comments.

- `def docstring(sym)`
    Get docstring for `sym` for functions ad classes

- `def parse_docstring(sym)`
    Parse a numpy-style docstring in `sym`

- `def isdataclass(s)`
    Check if `s` is a dataclass but not a dataclass' instance

- `def get_dataclass_source(s)`
    Get source code for dataclass `s`

- `def get_source(s)`
    Get source code for string, function object or dataclass `s`

- `def get_name(obj)`
    Get the name of `obj`

- `def qual_name(obj)`
    Get the qualified name of `obj`

- `@delegates(_docments) def docments(elt, full, **kwargs)`
    Generates a `docment`

- `def extract_docstrings(code)`
    Create a dict from function/class/method names to tuples of docstrings and param lists

## fastcore.docscrape

> Parse numpy-style docstrings

- `def strip_blank_lines(l)`
    Remove leading and trailing blank lines from a list of lines

- `class Reader`
    A line-based string reader.

    - `def __init__(self, data)`
    - `def __getitem__(self, n)`
    - `def reset(self)`
    - `def read(self)`
    - `def seek_next_non_empty_line(self)`
    - `def eof(self)`
    - `def read_to_condition(self, condition_func)`
    - `def read_to_next_empty_line(self)`
    - `def read_to_next_unindented_line(self)`
    - `def peek(self, n)`
    - `def is_empty(self)`

- `class ParseError`
    - `def __str__(self)`

- `class NumpyDocString`
    Parses a numpydoc string to an abstract representation

    - `def __init__(self, docstring, config)`
    - `def __iter__(self)`
    - `def __len__(self)`
    - `def __getitem__(self, key)`
    - `def __setitem__(self, key, val)`

- `def dedent_lines(lines, split)`
    Deindent a list of lines maximally

## fastcore.foundation

> The `L` class and helpers for it

- `@contextmanager def working_directory(path)`
    Change working directory to `path` and return to previous on exit.

- `def add_docs(cls, cls_doc, **docs)`
    Copy values from `docs` to `cls` docstrings, and confirm all public methods are documented

- `def docs(cls)`
    Decorator version of `add_docs`, using `_docs` dict

- `def coll_repr(c, max_n)`
    String repr of up to `max_n` items of (possibly lazy) collection `c`

- `def is_bool(x)`
    Check whether `x` is a bool or None

- `def mask2idxs(mask)`
    Convert bool mask or index list to index `L`

- `def is_indexer(idx)`
    Test whether `idx` will index a single item in a list

- `class CollBase`
    Base class for composing a list of `items`

    - `def __init__(self, items)`
    - `def __len__(self)`
    - `def __getitem__(self, k)`
    - `def __setitem__(self, k, v)`
    - `def __delitem__(self, i)`
    - `def __repr__(self)`
    - `def __iter__(self)`

- `class L`
    Behaves like a list of `items` but can also index with list of indices or masks

    - `def __init__(self, items, *rest)`
    - `def __getitem__(self, idx)`
    - `def copy(self)`
    - `def __setitem__(self, idx, o)`
        Set `idx` (can be list of indices, or mask, or int) items to `o` (which is broadcast if not iterable)

    - `def __eq__(self, b)`
    - `def sorted(self, key, reverse)`
    - `def __iter__(self)`
    - `def __contains__(self, b)`
    - `def __reversed__(self)`
    - `def __invert__(self)`
    - `def __repr__(self)`
    - `def __mul__(a, b)`
    - `def __add__(a, b)`
    - `def __radd__(a, b)`
    - `def __addi__(a, b)`
    - `@classmethod def split(cls, s, sep, maxsplit)`
    - `@classmethod def range(cls, a, b, step)`
    - `def map(self, f, *args, **kwargs)`
    - `def argwhere(self, f, negate, **kwargs)`
    - `def argfirst(self, f, negate)`
    - `def filter(self, f, negate, **kwargs)`
    - `def enumerate(self)`
    - `def renumerate(self)`
    - `def unique(self, sort, bidir, start)`
    - `def val2idx(self)`
    - `def cycle(self)`
    - `def map_dict(self, f, *args, **kwargs)`
    - `def map_first(self, f, g, *args, **kwargs)`
    - `def itemgot(self, *idxs)`
    - `def attrgot(self, k, default)`
    - `def starmap(self, f, *args, **kwargs)`
    - `def zip(self, cycled)`
    - `def zipwith(self, *rest)`
    - `def map_zip(self, f, *args, **kwargs)`
    - `def map_zipwith(self, f, *rest, **kwargs)`
    - `def shuffle(self)`
    - `def concat(self)`
    - `def reduce(self, f, initial)`
    - `def sum(self)`
    - `def product(self)`
    - `def setattrs(self, attr, val)`

- `def save_config_file(file, d, **kwargs)`
    Write settings dict to a new config file, or overwrite the existing one.

- `class Config`
    Reading and writing `ConfigParser` ini files

    - `def __init__(self, cfg_path, cfg_name, create, save, extra_files, types)`
    - `def __repr__(self)`
    - `def __setitem__(self, k, v)`
    - `def __contains__(self, k)`
    - `def save(self)`
    - `def __getattr__(self, k)`
    - `def __getitem__(self, k)`
    - `def get(self, k, default)`
    - `def path(self, k, default)`

## fastcore.imghdr

> Recognize image file formats based on their first few bytes.

- `def test_jpeg(h, f)`
    JPEG data with JFIF or Exif markers; and raw JPEG

- `def test_gif(h, f)`
    GIF ('87 and '89 variants)

- `def test_tiff(h, f)`
    TIFF (can be in Motorola or Intel byte order)

- `def test_rgb(h, f)`
    SGI image library

- `def test_pbm(h, f)`
    PBM (portable bitmap)

- `def test_pgm(h, f)`
    PGM (portable graymap)

- `def test_ppm(h, f)`
    PPM (portable pixmap)

- `def test_rast(h, f)`
    Sun raster file

- `def test_xbm(h, f)`
    X bitmap (X10 or X11)

## fastcore.imports

- `def is_iter(o)`
    Test whether `o` can be used in a `for` loop

- `def is_coll(o)`
    Test whether `o` is a collection (i.e. has a usable `len`)

- `def all_equal(a, b)`
    Compares whether `a` and `b` are the same length and have the same contents

- `def noop(x, *args, **kwargs)`
    Do nothing

- `def noops(self, x, *args, **kwargs)`
    Do nothing (method)

- `def isinstance_str(x, cls_name)`
    Like `isinstance`, except takes a type name instead of a type

- `def equals(a, b)`
    Compares `a` and `b` for equality; supports sublists, tensors and arrays too

- `def ipython_shell()`
    Same as `get_ipython` but returns `False` if not in IPython

- `def in_ipython()`
    Check if code is running in some kind of IPython environment

- `def in_colab()`
    Check if the code is running in Google Colaboratory

- `def in_jupyter()`
    Check if the code is running in a jupyter notebook

- `def in_notebook()`
    Check if the code is running in a jupyter notebook

- `def remove_prefix(text, prefix)`
    Temporary until py39 is a prereq

- `def remove_suffix(text, suffix)`
    Temporary until py39 is a prereq

## fastcore.meta

> Metaclasses

- `def test_sig(f, b)`
    Test the signature of an object

- `class FixSigMeta`
    A metaclass that fixes the signature on classes that override `__new__`

    - `def __new__(cls, name, bases, dict)`

- `class PrePostInitMeta`
    A metaclass that calls optional `__pre_init__` and `__post_init__` methods

    - `def __call__(cls, *args, **kwargs)`

- `class AutoInit`
    Same as `object`, but no need for subclasses to call `super().__init__`

    - `def __pre_init__(self, *args, **kwargs)`

- `class NewChkMeta`
    Metaclass to avoid recreating object passed to constructor

    - `def __call__(cls, x, *args, **kwargs)`

- `class BypassNewMeta`
    Metaclass: casts `x` to this class if it's of type `cls._bypass_type`

    - `def __call__(cls, x, *args, **kwargs)`

- `def empty2none(p)`
    Replace `Parameter.empty` with `None`

- `def anno_dict(f)`
    `__annotation__ dictionary with `empty` cast to `None`, returning empty if doesn't exist

- `def use_kwargs_dict(keep, **kwargs)`
    Decorator: replace `**kwargs` in signature with `names` params

- `def use_kwargs(names, keep)`
    Decorator: replace `**kwargs` in signature with `names` params

- `def delegates(to, keep, but)`
    Decorator: replace `**kwargs` in signature with params from `to`

- `def method(f)`
    Mark `f` as a method

- `def funcs_kwargs(as_method)`
    Replace methods in `cls._methods` with those from `kwargs`

## fastcore.net

> Network, HTTP, and URL functions

- `def urlquote(url)`
    Update url's path with `urllib.parse.quote`

- `def urlwrap(url, data, headers)`
    Wrap `url` in a urllib `Request` with `urlquote`

- `class HTTP4xxClientError`
    Base class for client exceptions (code 4xx) from `url*` functions


- `class HTTP5xxServerError`
    Base class for server exceptions (code 5xx) from `url*` functions


- `def urlopen(url, data, headers, timeout, **kwargs)`
    Like `urllib.request.urlopen`, but first `urlwrap` the `url`, and encode `data`

- `def urlread(url, data, headers, decode, return_json, return_headers, timeout, **kwargs)`
    Retrieve `url`, using `data` dict or `kwargs` to `POST` if present

- `def urljson(url, data, timeout)`
    Retrieve `url` and decode json

- `def urlclean(url)`
    Remove fragment, params, and querystring from `url` if present

- `def urlsave(url, dest, reporthook, headers, timeout)`
    Retrieve `url` and save based on its name

- `def urlvalid(x)`
    Test if `x` is a valid URL

- `def urlrequest(url, verb, headers, route, query, data, json_data)`
    `Request` for `url` with optional route params replaced by `route`, plus `query` string, and post `data`

- `@patch def summary(self, skip)`
    Summary containing full_url, headers, method, and data, removing `skip` from headers

- `def urlsend(url, verb, headers, decode, route, query, data, json_data, return_json, return_headers, debug, timeout)`
    Send request with `urlrequest`, converting result to json if `return_json`

- `def do_request(url, post, headers, **data)`
    Call GET or json-encoded POST on `url`, depending on `post`

- `def start_server(port, host, dgram, reuse_addr, n_queue)`
    Create a `socket` server on `port`, with optional `host`, of type `dgram`

- `def start_client(port, host, dgram)`
    Create a `socket` client on `port`, with optional `host`, of type `dgram`

- `def tobytes(s)`
    Convert `s` into HTTP-ready bytes format

- `def http_response(body, status, hdrs, **kwargs)`
    Create an HTTP-ready response, adding `kwargs` to `hdrs`

- `@threaded def recv_once(host, port)`
    Spawn a thread to receive a single HTTP request and store in `d['r']`

## fastcore.parallel

> Threading and multiprocessing functions

- `def threaded(process)`
    Run `f` in a `Thread` (or `Process` if `process=True`), and returns it

- `def startthread(f)`
    Like `threaded`, but start thread immediately

- `def startproc(f)`
    Like `threaded(True)`, but start Process immediately

- `class ThreadPoolExecutor`
    Same as Python's ThreadPoolExecutor, except can pass `max_workers==0` for serial execution

    - `def __init__(self, max_workers, on_exc, pause, **kwargs)`
    - `def map(self, f, items, *args, **kwargs)`

- `@delegates() class ProcessPoolExecutor`
    Same as Python's ProcessPoolExecutor, except can pass `max_workers==0` for serial execution

    - `def __init__(self, max_workers, on_exc, pause, **kwargs)`
    - `def map(self, f, items, *args, **kwargs)`

- `def parallel(f, items, *args, **kwargs)`
    Applies `func` in parallel to `items`, using `n_workers`

- `def run_procs(f, f_done, args)`
    Call `f` for each item in `args` in parallel, yielding `f_done`

- `def parallel_gen(cls, items, n_workers, **kwargs)`
    Instantiate `cls` in `n_workers` procs & call each on a subset of `items` in parallel.

## fastcore.py2pyi

- `def imp_mod(module_path, package)`
    Import dynamically the module referenced in `fn`

- `def has_deco(node, name)`
    Check if a function node `node` has a decorator named `name`

- `def create_pyi(fn, package)`
    Convert `fname.py` to `fname.pyi` by removing function bodies and expanding `delegates` kwargs

- `@call_parse def py2pyi(fname, package)`
    Convert `fname.py` to `fname.pyi` by removing function bodies and expanding `delegates` kwargs

- `@call_parse def replace_wildcards(path)`
    Expand wildcard imports in the specified Python file.

## fastcore.script

> A fast way to turn your python function into a script.

- `def store_true()`
    Placeholder to pass to `Param` for `store_true` action

- `def store_false()`
    Placeholder to pass to `Param` for `store_false` action

- `def bool_arg(v)`
    Use as `type` for `Param` to get `bool` behavior

- `class Param`
    A parameter in a function used in `anno_parser` or `call_parse`

    - `def __init__(self, help, type, opt, action, nargs, const, choices, required, default)`
    - `def set_default(self, d)`
    - `@property def pre(self)`
    - `@property def kwargs(self)`
    - `def __repr__(self)`

- `def anno_parser(func, prog)`
    Look at params (annotated with `Param`) in func and return an `ArgumentParser`

- `def args_from_prog(func, prog)`
    Extract args from `prog`

- `def call_parse(func, nested)`
    Decorator to create a simple CLI from `func` using `anno_parser`

## fastcore.style

> Fast styling for friendly CLIs.

- `class StyleCode`
    An escape sequence for styling terminal text.

    - `def __init__(self, name, code, typ)`
    - `def __str__(self)`

- `class Style`
    A minimal terminal text styler.

    - `def __init__(self, codes)`
    - `def __dir__(self)`
    - `def __getattr__(self, k)`
    - `def __call__(self, obj)`
    - `def __repr__(self)`

- `def demo()`
    Demonstrate all available styles and their codes.

## fastcore.test

> Helper functions to quickly write tests in notebooks

- `def test_fail(f, msg, contains, args, kwargs)`
    Fails with `msg` unless `f()` raises an exception and (optionally) has `contains` in `e.args`

- `def test(a, b, cmp, cname)`
    `assert` that `cmp(a,b)`; display inputs and `cname or cmp.__name__` if it fails

- `def nequals(a, b)`
    Compares `a` and `b` for `not equals`

- `def test_eq(a, b)`
    `test` that `a==b`

- `def test_eq_type(a, b)`
    `test` that `a==b` and are same type

- `def test_ne(a, b)`
    `test` that `a!=b`

- `def is_close(a, b, eps)`
    Is `a` within `eps` of `b`

- `def test_close(a, b, eps)`
    `test` that `a` is within `eps` of `b`

- `def test_is(a, b)`
    `test` that `a is b`

- `def test_shuffled(a, b)`
    `test` that `a` and `b` are shuffled versions of the same sequence of items

- `def test_stdout(f, exp, regex)`
    Test that `f` prints `exp` to stdout, optionally checking as `regex`

- `def test_fig_exists(ax)`
    Test there is a figure displayed in `ax`

- `class ExceptionExpected`
    Context manager that tests if an exception is raised

    - `def __init__(self, ex, regex)`
    - `def __enter__(self)`
    - `def __exit__(self, type, value, traceback)`

## fastcore.transform

> Definition of `Transform` and `Pipeline`

- `class Transform`
    Delegates (`__call__`,`decode`,`setup`) to (<code>encodes</code>,<code>decodes</code>,<code>setups</code>) if `split_idx` matches

    - `def __init__(self, enc, dec, split_idx, order)`
    - `@property def name(self)`
    - `def __call__(self, x, **kwargs)`
    - `def decode(self, x, **kwargs)`
    - `def __repr__(self)`
    - `def setup(self, items, train_setup)`

- `class InplaceTransform`
    A `Transform` that modifies in-place and just returns whatever it's passed


- `class DisplayedTransform`
    A transform with a `__repr__` that shows its attrs

    - `@property def name(self)`

- `class ItemTransform`
    A transform that always take tuples as items

    - `def __call__(self, x, **kwargs)`
    - `def decode(self, x, **kwargs)`

- `def get_func(t, name, *args, **kwargs)`
    Get the `t.name` (potentially partial-ized with `args` and `kwargs`) or `noop` if not defined

- `class Func`
    Basic wrapper around a `name` with `args` and `kwargs` to call on a given type

    - `def __init__(self, name, *args, **kwargs)`
    - `def __repr__(self)`
    - `def __call__(self, t)`

- `def compose_tfms(x, tfms, is_enc, reverse, **kwargs)`
    Apply all `func_nm` attribute of `tfms` on `x`, maybe in `reverse` order

- `def mk_transform(f)`
    Convert function `f` to `Transform` if it isn't already one

- `def gather_attrs(o, k, nm)`
    Used in __getattr__ to collect all attrs `k` from `self.{nm}`

- `def gather_attr_names(o, nm)`
    Used in __dir__ to collect all attrs `k` from `self.{nm}`

- `class Pipeline`
    A pipeline of composed (for encode/decode) transforms, setup with types

    - `def __init__(self, funcs, split_idx)`
    - `def setup(self, items, train_setup)`
    - `def add(self, ts, items, train_setup)`
    - `def __call__(self, o)`
    - `def __repr__(self)`
    - `def __getitem__(self, i)`
    - `def __setstate__(self, data)`
    - `def __getattr__(self, k)`
    - `def __dir__(self)`
    - `def decode(self, o, full)`
    - `def show(self, o, ctx, **kwargs)`

## fastcore.xdg

> XDG Base Directory Specification helpers.

- `def xdg_cache_home()`
    Path corresponding to `XDG_CACHE_HOME`

- `def xdg_config_dirs()`
    Paths corresponding to `XDG_CONFIG_DIRS`

- `def xdg_config_home()`
    Path corresponding to `XDG_CONFIG_HOME`

- `def xdg_data_dirs()`
    Paths corresponding to XDG_DATA_DIRS`

- `def xdg_data_home()`
    Path corresponding to `XDG_DATA_HOME`

- `def xdg_runtime_dir()`
    Path corresponding to `XDG_RUNTIME_DIR`

- `def xdg_state_home()`
    Path corresponding to `XDG_STATE_HOME`

## fastcore.xml

> Concise generation of XML.

- `class FT`
    A 'Fast Tag' structure, containing `tag`,`children`,and `attrs`

    - `def __init__(self, tag, cs, attrs, void_, **kwargs)`
    - `def __setattr__(self, k, v)`
    - `def __getattr__(self, k)`
    - `@property def list(self)`
    - `def get(self, k, default)`
    - `def __repr__(self)`
    - `def __add__(self, b)`
    - `def __getitem__(self, idx)`
    - `def __iter__(self)`

- `def ft(tag, *c, **kw)`
    Create an `FT` structure for `to_xml()`

- `def Html(*c, **kwargs)`
    An HTML tag, optionally preceeded by `!DOCTYPE HTML`

- `class Safe`
    - `def __html__(self)`

- `def to_xml(elm, lvl, indent, do_escape)`
    Convert `ft` element tree into an XML string

- `def highlight(s, lang)`
    Markdown to syntax-highlight `s` in language `lang`

## fastcore.xtras

> Utility functions used in the fastai library

- `def walk(path, symlinks, keep_file, keep_folder, skip_folder, func, ret_folders)`
    Generator version of `os.walk`, using functions to filter files and folders

- `def globtastic(path, recursive, symlinks, file_glob, file_re, folder_re, skip_file_glob, skip_file_re, skip_folder_re, func, ret_folders)`
    A more powerful `glob`, including regex matches, symlink handling, and skip parameters

- `@contextmanager def maybe_open(f, mode, **kwargs)`
    Context manager: open `f` if it is a path (and close on exit)

- `def mkdir(path, exist_ok, parents, overwrite, **kwargs)`
    Creates and returns a directory defined by `path`, optionally removing previous existing directory if `overwrite` is `True`

- `def image_size(fn)`
    Tuple of (w,h) for png, gif, or jpg; `None` otherwise

- `def bunzip(fn)`
    bunzip `fn`, raising exception if output already exists

- `def loads(s, **kw)`
    Same as `json.loads`, but handles `None`

- `def loads_multi(s)`
    Generator of >=0 decoded json dicts, possibly with non-json ignored text at start and end

- `def dumps(obj, **kw)`
    Same as `json.dumps`, but uses `ujson` if available

- `def untar_dir(fname, dest, rename, overwrite)`
    untar `file` into `dest`, creating a directory if the root contains more than one item

- `def repo_details(url)`
    Tuple of `owner,name` from ssh or https git repo `url`

- `def run(cmd, *rest)`
    Pass `cmd` (splitting with `shlex` if string) to `subprocess.run`; return `stdout`; raise `IOError` if fails

- `def open_file(fn, mode, **kwargs)`
    Open a file, with optional compression if gz or bz2 suffix

- `def save_pickle(fn, o)`
    Save a pickle file, to a file name or opened file

- `def load_pickle(fn)`
    Load a pickle file from a file name or opened file

- `def parse_env(s, fn)`
    Parse a shell-style environment string or file

- `def expand_wildcards(code)`
    Expand all wildcard imports in the given code string.

- `def dict2obj(d, list_func, dict_func)`
    Convert (possibly nested) dicts (or lists of dicts) to `AttrDict`

- `def obj2dict(d)`
    Convert (possibly nested) AttrDicts (or lists of AttrDicts) to `dict`

- `def repr_dict(d)`
    Print nested dicts and lists, such as returned by `dict2obj`

- `def is_listy(x)`
    `isinstance(x, (tuple,list,L,slice,Generator))`

- `def mapped(f, it)`
    map `f` over `it`, unless it's not listy, in which case return `f(it)`

- `@patch def readlines(self, hint, encoding)`
    Read the content of `self`

- `@patch def read_json(self, encoding, errors)`
    Same as `read_text` followed by `loads`

- `@patch def mk_write(self, data, encoding, errors, mode)`
    Make all parent dirs of `self`, and write `data`

- `@patch def relpath(self, start)`
    Same as `os.path.relpath`, but returns a `Path`, and resolves symlinks

- `@patch def ls(self, n_max, file_type, file_exts)`
    Contents of path as a list

- `@patch def delete(self)`
    Delete a file, symlink, or directory tree

- `class IterLen`
    Base class to add iteration to anything supporting `__len__` and `__getitem__`

    - `def __iter__(self)`

- `@docs class ReindexCollection`
    Reindexes collection `coll` with indices `idxs` and optional LRU cache of size `cache`

    - `def __init__(self, coll, idxs, cache, tfm)`
    - `def __getitem__(self, i)`
    - `def __len__(self)`
    - `def reindex(self, idxs)`
    - `def shuffle(self)`
    - `def cache_clear(self)`
    - `def __getstate__(self)`
    - `def __setstate__(self, s)`

- `def get_source_link(func)`
    Return link to `func` in source code

- `def truncstr(s, maxlen, suf, space)`
    Truncate `s` to length `maxlen`, adding suffix `suf` if truncated

- `def sparkline(data, mn, mx, empty_zero)`
    Sparkline for `data`, with `None`s (and zero, if `empty_zero`) shown as empty column

- `def modify_exception(e, msg, replace)`
    Modifies `e` with a custom message attached

- `def round_multiple(x, mult, round_down)`
    Round `x` to nearest multiple of `mult`

- `def set_num_threads(nt)`
    Get numpy (and others) to use `nt` threads

- `def join_path_file(file, path, ext)`
    Return `path/file` if file is a string or a `Path`, file otherwise

- `def autostart(g)`
    Decorator that automatically starts a generator

- `class EventTimer`
    An event timer with history of `store` items of time `span`

    - `def __init__(self, store, span)`
    - `def add(self, n)`
        Record `n` events

    - `@property def duration(self)`
    - `@property def freq(self)`

- `def stringfmt_names(s)`
    Unique brace-delimited names in `s`

- `class PartialFormatter`
    A `string.Formatter` that doesn't error on missing fields, and tracks missing fields and unused args

    - `def __init__(self)`
    - `def get_field(self, nm, args, kwargs)`
    - `def check_unused_args(self, used, args, kwargs)`

- `def partial_format(s, **kwargs)`
    string format `s`, ignoring missing field errors, returning missing and extra fields

- `def utc2local(dt)`
    Convert `dt` from UTC to local time

- `def local2utc(dt)`
    Convert `dt` from local to UTC time

- `def trace(f)`
    Add `set_trace` to an existing function `f`

- `@contextmanager def modified_env(*delete, **replace)`
    Context manager temporarily modifying `os.environ` by deleting `delete` and replacing `replace`

- `class ContextManagers`
    Wrapper for `contextlib.ExitStack` which enters a collection of context managers

    - `def __init__(self, mgrs)`
    - `def __enter__(self)`
    - `def __exit__(self, *args, **kwargs)`

- `def shufflish(x, pct)`
    Randomly relocate items of `x` up to `pct` of `len(x)` from their starting location

- `def console_help(libname)`
    Show help for all console scripts from `libname`

- `def hl_md(s, lang, show)`
    Syntax highlight `s` using `lang`.

- `def type2str(typ)`
    Stringify `typ`

- `class Unset`
    - `def __repr__(self)`
    - `def __str__(self)`
    - `def __bool__(self)`
    - `@property def name(self)`

- `def nullable_dc(cls)`
    Like `dataclass`, but default of `UNSET` added to fields without defaults

- `def flexiclass(cls)`
    Convert `cls` into a `dataclass` like `make_nullable`. Converts in place and also returns the result.

- `def asdict(o)`
    Convert `o` to a `dict`, supporting dataclasses, namedtuples, iterables, and `__dict__` attrs.

- `def is_typeddict(cls)`
    Check if `cls` is a `TypedDict`

- `def is_namedtuple(cls)`
    `True` if `cls` is a namedtuple type

- `def flexicache(*funcs)`
    Like `lru_cache`, but customisable with policy `funcs`

- `def time_policy(seconds)`
    A `flexicache` policy that expires cached items after `seconds` have passed

- `def mtime_policy(filepath)`
    A `flexicache` policy that expires cached items after `filepath` modified-time changes

- `def timed_cache(seconds, maxsize)`
    Like `lru_cache`, but also with time-based eviction

