## Project description

[![https://travis-ci.com/ICRAR/ijson.svg?branch=master](https://warehouse-camo.ingress.cmh1.psfhosted.org/27b4793325d64d08b165da70db7a735a8d1b5c9c/68747470733a2f2f7472617669732d63692e636f6d2f49435241522f696a736f6e2e7376673f6272616e63683d6d6173746572)](https://travis-ci.com/ICRAR/ijson) [![https://ci.appveyor.com/api/projects/status/32wiho6ojw3eakp8/branch/master?svg=true](https://warehouse-camo.ingress.cmh1.psfhosted.org/9fff408bcc1e78534a3ef4f3ba6cc2416f045f3a/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f33327769686f366f6a773365616b70382f6272616e63682f6d61737465723f7376673d74727565)](https://ci.appveyor.com/project/rtobar/ijson/branch/master) [![https://coveralls.io/repos/github/ICRAR/ijson/badge.svg?branch=master](https://warehouse-camo.ingress.cmh1.psfhosted.org/ceeea84560bed04be709d849b453b01b4ffaba64/68747470733a2f2f636f766572616c6c732e696f2f7265706f732f6769746875622f49435241522f696a736f6e2f62616467652e7376673f6272616e63683d6d6173746572)](https://coveralls.io/github/ICRAR/ijson?branch=master) [![https://badge.fury.io/py/ijson.svg](https://warehouse-camo.ingress.cmh1.psfhosted.org/28d2fa703ca0aa66002fb979b89f0d150958dbe9/68747470733a2f2f62616467652e667572792e696f2f70792f696a736f6e2e737667)](https://badge.fury.io/py/ijson) [![https://img.shields.io/pypi/pyversions/ijson.svg](https://warehouse-camo.ingress.cmh1.psfhosted.org/11e3376eae2f3e90baa8483b934e3fc679331e48/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f696a736f6e2e737667)](https://pypi.python.org/pypi/ijson) [![https://img.shields.io/pypi/dd/ijson.svg](https://warehouse-camo.ingress.cmh1.psfhosted.org/d0388d4e14270deddb1f1c20773e1def8ffe99c3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f64642f696a736f6e2e737667)](https://pypi.python.org/pypi/ijson) [![https://img.shields.io/pypi/dw/ijson.svg](https://warehouse-camo.ingress.cmh1.psfhosted.org/b04b5ae36a454d258748c391c0ef6734106c8e57/68747470733a2f2f696d672e736869656c64732e696f2f707970692f64772f696a736f6e2e737667)](https://pypi.python.org/pypi/ijson) [![https://img.shields.io/pypi/dm/ijson.svg](https://warehouse-camo.ingress.cmh1.psfhosted.org/2a6412249e514adb59edd719666e50d736c64cc4/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f696a736f6e2e737667)](https://pypi.python.org/pypi/ijson)

## ijson

Ijson 是一个具有标准 Python 迭代器接口的迭代 JSON 解析器。

- [安装](https://pypi.org/project/ijson/#installation)
- 用法
  - [高级接口](https://pypi.org/project/ijson/#high-level-interfaces)
  - [底层接口](https://pypi.org/project/ijson/#lower-level-interfaces)
  - [`字节`/`字符串`支持](https://pypi.org/project/ijson/#bytes-str-support)
  - [`异步` 支持](https://pypi.org/project/ijson/#asyncio-support)
  - [拦截事件](https://pypi.org/project/ijson/#intercepting-events)
  - [推送接口](https://pypi.org/project/ijson/#push-interfaces)
- [选项](https://pypi.org/project/ijson/#id1)
- [活动](https://pypi.org/project/ijson/#events)
- [前缀](https://pypi.org/project/ijson/#id2)
- [后缀](https://pypi.org/project/ijson/#id3)
- [性能提示](https://pypi.org/project/ijson/#performance-tips)
- [常见问题](https://pypi.org/project/ijson/#id5)
- [致谢](https://pypi.org/project/ijson/#acknowledgements)

### [安装](https://pypi.org/project/ijson/#id7)

Ijson 托管在 PyPI 中，因此您应该能够通过`pip`安装它：

```
pip install ijson
```

为主要平台（Linux、MacOS、Windows）和 python 版本（2.7、3.5+）提供了二进制轮子。这些是 通过 Travis CI使用[cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/)自动构建和发布的。

### [用法](https://pypi.org/project/ijson/#id8)

所有用法示例都将使用描述地理对象的 JSON 文档：

```
{
  "earth": {
    "europe": [
      {"name": "Paris", "type": "city", "info": { ... }},
      {"name": "Thames", "type": "river", "info": { ... }},
      // ...
    ],
    "america": [
      {"name": "Texas", "type": "state", "info": { ... }},
      // ...
    ]
  }
}
```

#### 高级接口

最常见的用法是让 ijson 从位于前缀下的 JSON 流中产生本机 Python 对象。这是使用`items`函数完成的。以下是处理所有欧洲城市的方法：

```
import ijson

f = urlopen('http://.../')
objects = ijson.items(f, 'earth.europe.item')
cities = (o for o in objects if o['type'] == 'city')
for city in cities:
    do_something_with(city)
```

有关如何构建前缀，请参阅下面的[前缀](https://pypi.org/project/ijson/#prefix)部分。

其他时候，迭代对象成员而不是对象本身可能很有用（例如，当对象太大时）。在这种情况下，可以改用`kvitems`函数：

```
import ijson

f = urlopen('http://.../')
european_places = ijson.kvitems(f, 'earth.europe.item')
names = (v for k, v in european_places if k == 'name')
for name in names:
    do_something_with(name)
```

#### [底层接口](https://pypi.org/project/ijson/#id10)

有时，在处理特别大的 JSON 负载时，甚至不构建单独的 Python 对象并立即对单独的事件做出反应以产生某些结果可能是值得的。这是使用`parse`函数实现的：

```
import ijson

parser = ijson.parse(urlopen('http://.../'))
stream.write('<geo>')
for prefix, event, value in parser:
    if (prefix, event) == ('earth', 'map_key'):
        stream.write('<%s>' % value)
        continent = value
    elif prefix.endswith('.name'):
        stream.write('<object name="%s"/>' % value)
    elif (prefix, event) == ('earth.%s' % continent, 'end_map'):
        stream.write('</%s>' % continent)
stream.write('</geo>')
```

更简单的是能够对单个事件做出反应，甚至无需使用`basic_parse`函数计算前缀：

```
import ijson

events = ijson.basic_parse(urlopen('http://.../'))
num_names = sum(1 for event, value in events
                if event == 'map_key' and value == 'name')
```

#### [`字节`/`字符串`支持](https://pypi.org/project/ijson/#id11)

尽管通常不是它们的运行方式，但上面的所有函数也直接接受 `字节`和`str`对象（以及python 2.7 中的`unicode`）作为输入。然后将它们在内部包装成一个文件对象，并进一步处理。这对于测试和原型设计很有用，但在现实生活场景中可能不是非常有用。

#### [`异步`支持](https://pypi.org/project/ijson/#id12)

在 python 3.5+ 中，上述所有方法也适用于类文件异步对象，因此它们可以异步迭代。换句话说，是这样的：

```
import asyncio
import ijson

async def run():
   f = await async_urlopen('http://..../')
   async for object in ijson.items(f, 'earth.europe.item'):
      if object['type'] == 'city':
         do_something_with(city)
asyncio.run(run())
```

还存在一组显式的`*_async`函数，提供相同的功能，但如果给它们提供了类似文件的异步对象以外的任何东西，它们就会失败。（所以上面的例子也可以使用`ijson.items_async`编写）。事实上，在 ijson 3.0 版中，这是访问`asyncio`支持的唯一方法。

#### [Intercepting events](https://pypi.org/project/ijson/#id13)

The four routines shown above internally chain against each other: tuples generated by `basic_parse` are the input for `parse`, whose results are the input to `kvitems` and `items`.

Normally users don’t see this interaction, as they only care about the final output of the function they invoked, but there are occasions when tapping into this invocation chain this could be handy. This is supported by passing the output of one function (i.e., an iterable of events, usually a generator) as the input of another, opening the door for user event filtering or injection.

For instance if one wants to skip some content before full item parsing:

```
import io
import ijson

parse_events = ijson.parse(io.BytesIO(b'["skip", {"a": 1}, {"b": 2}, {"c": 3}]'))
while True:
    prefix, event, value = next(parse_event)
    if value == "skip":
        break
for obj in ijson.items(parse_events, 'item')
    print(obj)
```

Note that this interception only makes sense for the `basic_parse -> parse`, `parse -> items` and `parse -> kvitems` interactions.

#### [Push interfaces](https://pypi.org/project/ijson/#id14)

All examples above use a file-like object as the data input (both the normal case, and for `asyncio` support), and hence are “pull” interfaces, with the library reading data as necessary. If for whatever reason it’s not possible to use such method, you can still **push** data through yet a different interface: [coroutines](https://www.python.org/dev/peps/pep-0342/) (via generators, not `asyncio` coroutines). Coroutines effectively allow users to send data to them at any point in time, with a final *target* coroutine-like object receiving the results.

In the following example the user is doing the reading instead of letting the library do it:

```
import ijson

@ijson.coroutine
def print_cities():
   while True:
      obj = (yield)
      if obj['type'] != 'city':
         continue
      print(obj)

coro = ijson.items_coro(print_cities(), 'earth.europe.item')
f = urlopen('http://.../')
for chunk in iter(functools.partial(f.read, buf_size)):
   coro.send(chunk)
coro.close()
```

All four ijson iterators have a `*_coro` counterpart that work by pushing data into them. Instead of receiving a file-like object and option buffer size as arguments, they receive a single `target` argument, which should be a coroutine-like object (anything implementing a `send` method) through which results will be published.

An alternative to providing a coroutine is to use `ijson.sendable_list` to accumulate results, providing the list is cleared after each parsing iteration, like this:

```
import ijson

events = ijson.sendable_list()
coro = ijson.items_coro(events, 'earth.europe.item')
f = urlopen('http://.../')
for chunk in iter(functools.partial(f.read, buf_size)):
   coro.send(chunk)
   process_accumulated_events(events)
   del events[:]
coro.close()
process_accumulated_events(events)
```



### [Options](https://pypi.org/project/ijson/#id15)

Additional options are supported by **all** ijson functions to give users more fine-grained control over certain operations:

- The `use_float` option (defaults to `False`) controls how non-integer values are returned to the user. If set to `True` users receive `float()` values; otherwise `Decimal` values are constructed. Note that building `float` values is usually faster, but on the other hand there might be loss of precision (which most applications will not care about) and will raise an exception when overflow occurs (e.g., if `1e400` is encountered). This option also has the side-effect that integer numbers bigger than `2^64` (but *sometimes* `2^32`, see [backends](https://pypi.org/project/ijson/#backends)) will also raise an overflow error, due to similar reasons. Future versions of ijson might change the default value of this option to `True`.
- The `multiple_values` option (defaults to `False`) controls whether multiple top-level values are supported. JSON content should contain a single top-level value (see [the JSON Grammar](https://tools.ietf.org/html/rfc7159#section-2)). However there are plenty of JSON files out in the wild that contain multiple top-level values, often separated by newlines. By default ijson will fail to process these with a `parse error: trailing garbage` error unless `multiple_values=True` is specified.
- Similarly the `allow_comments` option (defaults to `False`) controls whether C-style comments (e.g., `/* a comment */`), which are not supported by the JSON standard, are allowed in the content or not.
- For functions taking a file-like object, an additional `buf_size` option (defaults to `65536` or 64KB) specifies the amount of bytes the library should attempt to read each time.
- The `items` and `kvitems` functions, and all their variants, have an optional `map_type` argument (defaults to `dict`) used to construct objects from the JSON stream. This should be a dict-like type supporting item assignment.

### [Events](https://pypi.org/project/ijson/#id16)

When using the lower-level `ijson.parse` function, three-element tuples are generated containing a prefix, an event name, and a value. Events will be one of the following:

- `start_map` and `end_map` indicate the beginning and end of a JSON object, respectively. They carry a `None` as their value.
- `start_array` and `end_array` indicate the beginning and end of a JSON array, respectively. They also carry a `None` as their value.
- `map_key` indicates the name of a field in a JSON object. Its associated value is the name itself.
- `null`, `boolean`, `integer`, `double`, `number` and `string` all indicate actual content, which is stored in the associated value.



### [Prefix](https://pypi.org/project/ijson/#id17)

A prefix represents the context within a JSON document where an event originates at. It works as follows:

- It starts as an empty string.
- A `` part is appended when the parser starts parsing the contents of a JSON object member called `name`, and removed once the content finishes.
- A literal `item` part is appended when the parser is parsing elements of a JSON array, and removed when the array ends.
- Parts are separated by `.`.

When using the `ijson.items` function, the prefix works as the selection for which objects should be automatically built and returned by ijson.



### [Backends](https://pypi.org/project/ijson/#id18)

Ijson provides several implementations of the actual parsing in the form of backends located in ijson/backends:

- `yajl2_c`: a C extension using [YAJL](http://lloyd.github.com/yajl/) 2.x. This is the fastest, but *might* require a compiler and the YAJL development files to be present when installing this package. Binary wheel distributions exist for major platforms/architectures to spare users from having to compile the package.
- `yajl2_cffi`: wrapper around [YAJL](http://lloyd.github.com/yajl/) 2.x using CFFI.
- `yajl2`: wrapper around YAJL 2.x using ctypes, for when you can’t use CFFI for some reason.
- `yajl`: deprecated YAJL 1.x + ctypes wrapper, for even older systems.
- `python`: pure Python parser, good to use with PyPy

You can import a specific backend and use it in the same way as the top level library:

```
import ijson.backends.yajl2_cffi as ijson

for item in ijson.items(...):
    # ...
```

Importing the top level library as `import ijson` uses the first available backend in the same order of the list above, and its name is recorded under `ijson.backend`. If the `IJSON_BACKEND` environment variable is set its value takes precedence and is used to select the default backend.

You can also use the `ijson.get_backend` function to get a specific backend based on a name:

```
backend = ijson.get_backend('yajl2_c')
for item in backend.items(...):
    # ...
```

### [Performance tips](https://pypi.org/project/ijson/#id19)

In more-or-less decreasing order, these are the most common actions you can take to ensure you get most of the performance out of ijson:

- Make sure you use the fastest backend available. See [backends](https://pypi.org/project/ijson/#backends) for details.
- If you know your JSON data contains only numbers that are “well behaved” consider turning on the `use_float` option. See [options](https://pypi.org/project/ijson/#options) for details.
- Make sure you feed ijson with binary data instead of text data. See [faq](https://pypi.org/project/ijson/#faq) #1 for details.
- Play with the `buf_size` option, as depending on your data source and your system a value different from the default might show better performance. See [options](https://pypi.org/project/ijson/#options) for details.



### [FAQ](https://pypi.org/project/ijson/#id20)

1. **Q**: Does ijson work with `bytes` or `str` values?

   **A**: In short: both are accepted as input, outputs are only `str`.

   All ijson functions expecting a file-like object should ideally be given one that is opened in binary mode (i.e., its `read` function returns `bytes` objects, not `str`). However if a text-mode file object is given then the library will automatically encode the strings into UTF-8 bytes. A warning is currently issued (but not visible by default) alerting users about this automatic conversion.

   On the other hand ijson always returns text data (JSON string values, object member names, event names, etc) as `str` objects in python 3, and `unicode` objects in python 2.7. This mimics the behavior of the system `json` module.

2. **Q**: How are numbers dealt with?

   **A**: ijson returns `int` values for integers and `decimal.Decimal` values for floating-point numbers. This is mostly because of historical reasons. Since 3.1 a new `use_float` option (defaults to `False`) is available to return `float` values instead. See the [options](https://pypi.org/project/ijson/#options) section for details.

3. **Q**: I’m getting an `UnicodeDecodeError`, or an `IncompleteJSONError` with no message

   **A**: This error is caused by byte sequences that are not valid in UTF-8. In other words, the data given to ijson is not *really* UTF-8 encoded, or at least not properly.

   Depending on where the data comes from you have different options:

   - If you have control over the source of the data, fix it.
   - If you have a way to intercept the data flow, do so and pass it through a “byte corrector”. For instance, if you have a shell pipeline feeding data through `stdin` into your process you can add something like `... | iconv -f utf8 -t utf8 -c | ...` in between to correct invalid byte sequences.
   - If you are working purely in python, you can create a UTF-8 decoder using codecs’ [incrementaldecoder](https://docs.python.org/3/library/codecs.html#codecs.getincrementaldecoder) to leniently decode your bytes into strings, and feed those strings (using a file-like class) into ijson (see our [string_reader_async internal class](https://github.com/ICRAR/ijson/blob/0157f3c65a7986970030d3faa75979ee205d3806/ijson/utils35.py#L19) for some inspiration).

   In the future ijson might offer something out of the box to deal with invalid UTF-8 byte sequences.

4. **Q**: I’m getting `parse error: trailing garbage` or `Additional data found` errors

   **A**: This error signals that the input contains more data than the top-level JSON value it’s meant to contain. This is *usually* caused by JSON data sources containing multiple values, and is *usually* solved by passing the `multiple_values=True` to the ijson function in use. See the [options](https://pypi.org/project/ijson/#options) section for details.

5. **Q**: Are there any differences between the backends?

   **A**: Apart from their performance, all backends are designed to support the same capabilities. There are however some small known differences:

   - The `yajl` backend doesn’t support `multiple_values=True`. It also doesn’t complain about additional data found after the end of the top-level JSON object. When using `use_float=True` it also doesn’t properly support values greater than 2^32 in 32-bit platforms or Windows. Numbers with leading zeros are not reported as invalid (although they are invalid JSON numbers). Incomplete JSON tokens at the end of an incomplete document (e.g., `{"a": fals`) are not reported as `IncompleteJSONError`.
   - The `python` backend doesn’t support `allow_comments=True` It also internally works with `str` objects, not `bytes`, but this is an internal detail that users shouldn’t need to worry about, and might change in the future.

### [Acknowledgements](https://pypi.org/project/ijson/#id21)

ijson was originally developed and actively maintained until 2016 by [Ivan Sagalaev](http://softwaremaniacs.org/). In 2019 he [handed over](https://github.com/isagalaev/ijson/pull/58#issuecomment-500596815) the maintenance of the project and the PyPI ownership.

Python parser in ijson is relatively simple thanks to [Douglas Crockford](http://www.crockford.com/) who invented a strict, easy to parse syntax.

The [YAJL](http://lloyd.github.com/yajl/) library by [Lloyd Hilaiel](http://lloyd.io/) is the most popular and efficient way to parse JSON in an iterative fashion.

Ijson was inspired by [yajl-py](http://pykler.github.com/yajl-py/) wrapper by [Hatem Nassrat](http://www.nassrat.ca/). Though ijson borrows almost nothing from the actual yajl-py code it was used as an example of integration with yajl using ctypes.