Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> text='hello'
>>> text.upper()
'HELLO'
>>> 
========== RESTART: C:/Users/ESOUSSH/Desktop/DefiningExceptions.py ==========
Traceback (most recent call last):
  File "C:/Users/ESOUSSH/Desktop/DefiningExceptions.py", line 1, in <module>
    class MyError(Excecption):
NameError: name 'Excecption' is not defined
>>> 
========== RESTART: C:/Users/ESOUSSH/Desktop/DefiningExceptions.py ==========
Traceback (most recent call last):
  File "C:/Users/ESOUSSH/Desktop/DefiningExceptions.py", line 9, in <module>
    raise(MyError)
TypeError: __init__() missing 1 required positional argument: 'value'
>>> 
========== RESTART: C:/Users/ESOUSSH/Desktop/DefiningExceptions.py ==========
A new Exception occured:  6
>>> help(Exception)
Help on class Exception in module builtins:

class Exception(BaseException)
 |  Common base class for all non-exit exceptions.
 |  
 |  Method resolution order:
 |      Exception
 |      BaseException
 |      object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseException:
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __setstate__(...)
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  with_traceback(...)
 |      Exception.with_traceback(tb) --
 |      set self.__traceback__ to tb and return self.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |  
 |  __cause__
 |      exception cause
 |  
 |  __context__
 |      exception context
 |  
 |  __dict__
 |  
 |  __suppress_context__
 |  
 |  __traceback__
 |  
 |  args

>>> locals()['__builtins__']
<module 'builtins' (built-in)>
>>> import gc
>>> dir(gc)
['DEBUG_COLLECTABLE', 'DEBUG_LEAK', 'DEBUG_SAVEALL', 'DEBUG_STATS', 'DEBUG_UNCOLLECTABLE', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'callbacks', 'collect', 'disable', 'enable', 'garbage', 'get_count', 'get_debug', 'get_objects', 'get_referents', 'get_referrers', 'get_stats', 'get_threshold', 'is_tracked', 'isenabled', 'set_debug', 'set_threshold']
>>> import timeit
>>> dir(timeit)
['Timer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_globals', 'default_number', 'default_repeat', 'default_timer', 'dummy_src_name', 'gc', 'itertools', 'main', 'reindent', 'repeat', 'sys', 'template', 'time', 'timeit']
>>> import numpy
>>> dir(numpy)
['ALLOW_THREADS', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_distributor_init', '_globals', '_import_tools', '_mat', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'add_newdocs', 'alen', 'all', 'allclose', 'alltrue', 'alterdot', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'bench', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'histogram', 'histogram2d', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isinf', 'isnan', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'pkgload', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'power', 'ppmt', 'print_function', 'prod', 'product', 'promote_types', 'ptp', 'put', 'putmask', 'pv', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'restoredot', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']
>>> len(dir(numpy))
605
>>> import numpy as np
>>> arr=np.array([[1,2,3],[4,5,6]])
>>> type(arr)
<class 'numpy.ndarray'>
>>> arr.ndim
2
>>> arr.shape
(2, 3)
>>> arr.size
6
>>> arr.dtype
dtype('int32')
>>> 
============= RESTART: C:/Users/ESOUSSH/Desktop/MakingRequest.py =============
Traceback (most recent call last):
  File "C:/Users/ESOUSSH/Desktop/MakingRequest.py", line 6, in <module>
    data=r.json()
  File "C:\Python35\lib\site-packages\requests\models.py", line 850, in json
    return complexjson.loads(self.text, **kwargs)
  File "C:\Python35\lib\site-packages\simplejson\__init__.py", line 516, in loads
    return _default_decoder.decode(s)
  File "C:\Python35\lib\site-packages\simplejson\decoder.py", line 374, in decode
    obj, end = self.raw_decode(s)
  File "C:\Python35\lib\site-packages\simplejson\decoder.py", line 404, in raw_decode
    return self.scan_once(s, idx=_w(s, idx).end())
  File "C:\Python35\lib\site-packages\simplejson\scanner.py", line 127, in scan_once
    return _scan_once(string, idx)
  File "C:\Python35\lib\site-packages\simplejson\scanner.py", line 118, in _scan_once
    raise JSONDecodeError(errmsg, string, idx)
simplejson.scanner.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
>>> import re
>>> print(dir(re),len(dir(re)))
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alphanum_str', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copyreg', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template'] 57
>>> for x in dir(re): print(x)

A
ASCII
DEBUG
DOTALL
I
IGNORECASE
L
LOCALE
M
MULTILINE
S
Scanner
T
TEMPLATE
U
UNICODE
VERBOSE
X
_MAXCACHE
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
__version__
_alphanum_bytes
_alphanum_str
_cache
_cache_repl
_compile
_compile_repl
_expand
_locale
_pattern_type
_pickle
_subx
compile
copyreg
error
escape
findall
finditer
fullmatch
match
purge
search
split
sre_compile
sre_parse
sub
subn
sys
template
>>> import re
>>> p=re.compile('[a-e]')
>>> print(p.findall("Aye, said Mr. Gibenson Stark"))
['e', 'a', 'd', 'b', 'e', 'a']
>>> p=re.compile('[a-e]||[A-E]')
>>> print(p.findall("Aye, said Mr. Gibenson Stark"))
['', '', 'e', '', '', '', 'a', '', 'd', '', '', '', '', '', '', '', 'b', 'e', '', '', '', '', '', '', '', 'a', '', '', '']
>>> p=re.compile('[a-e]&&[A-E]')
>>> print(p.findall("Aye, said Mr. Gibenson Stark"))
[]
>>> p=re.compile('[A-E]')
>>> print(p.findall("Aye, said Mr. Gibenson Stark"))
['A']
>>> p=re.compile('a,e,i,o,u')
>>> print(p.findall("Aye, said Mr. Gibenson Stark"))
[]
>>> dir(re.split)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> re.split()
