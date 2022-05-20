## Silence

用于在音频片段中查找/处理静音的各种功能。有关创建无声音频片段的信息，请参见 AudioSegment.silent().

### silence.detect_silence()

返回以毫秒为单位的所有静默部分[开始，结束]的列表。 detect_nonsilent() 的反向函数. 可能非常慢，因为它必须迭代整个段。

```
from pydub import AudioSegment, silence

print(silence.detect_silence(AudioSegment.silent(2000)))
# [[0, 2000]]
```

**Supported keyword arguments**:

- `min_silence_len` | example: `500` | default: 1000 The minimum length for silent sections in milliseconds. If it is greater than the length of the audio segment an empty list will be returned.
- `silence_thresh` | example: `-20` | default: -16 The upper bound for how quiet is silent in dBFS.
- `seek_step` | example: `5` | default: 1 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.

### silence.detect_nonsilent()

Returns a list of all silent sections [start, end] in milliseconds of audio_segment. Inverse of detect_silence() and has all the same arguments. Can be very slow since it has to iterate over the whole segment.

**Supported keyword arguments**:

- `min_silence_len` | example: `500` | default: 1000 The minimum length for silent sections in milliseconds. If it is greater than the length of the audio segment an empty list will be returned.
- `silence_thresh` | example: `-20` | default: -16 The upper bound for how quiet is silent in dBFS.
- `seek_step` | example: `5` | default: 1 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.

### silence.split_on_silence()

返回在静默段上拆分音频段的音频段列表。

**Supported keyword arguments**:

- `min_silence_len` | example: `500` | default: 1000 The minimum length for silent sections in milliseconds. If it is greater than the length of the audio segment an empty list will be returned.
- `silence_thresh` | example: `-20` | default: -16 The upper bound for how quiet is silent in dBFS.
- `seek_step` | example: `5` | default: 1 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.
- `keep_silence` ~ example: True | default: 100 How much silence to keep in ms or a bool. leave some silence at the beginning and end of the chunks. Keeps the sound from sounding like it is abruptly cut off. When the length of the silence is less than the keep_silence duration it is split evenly between the preceding and following non-silent segments. If True is specified, all the silence is kept, if False none is kept.

### silence.detect_leading_silence()

Returns the millisecond/index that the leading silence ends. If there is no end it will return the length of the audio_segment.

```
from pydub import AudioSegment, silence

print(silence.detect_silence(AudioSegment.silent(2000)))
# 2000
```

**Supported keyword arguments**:

- `silence_thresh` | example: `-20` | default: -50 The upper bound for how quiet is silent in dBFS.
- `chunk_size` | example: `5` | default: 10 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.



## Silence

Various functions for finding/manipulating silence in AudioSegments. For creating silent AudioSegments, see AudioSegment.silent().

### silence.detect_silence()

Returns a list of all silent sections [start, end] in milliseconds of audio_segment. Inverse of detect_nonsilent(). Can be very slow since it has to iterate over the whole segment.

```
from pydub import AudioSegment, silence

print(silence.detect_silence(AudioSegment.silent(2000)))
# [[0, 2000]]
```

**Supported keyword arguments**:

- `min_silence_len` | example: `500` | default: 1000 The minimum length for silent sections in milliseconds. If it is greater than the length of the audio segment an empty list will be returned.
- `silence_thresh` | example: `-20` | default: -16 The upper bound for how quiet is silent in dBFS.
- `seek_step` | example: `5` | default: 1 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.

### silence.detect_nonsilent()

Returns a list of all silent sections [start, end] in milliseconds of audio_segment. Inverse of detect_silence() and has all the same arguments. Can be very slow since it has to iterate over the whole segment.

**Supported keyword arguments**:

- `min_silence_len` | example: `500` | default: 1000 The minimum length for silent sections in milliseconds. If it is greater than the length of the audio segment an empty list will be returned.
- `silence_thresh` | example: `-20` | default: -16 The upper bound for how quiet is silent in dBFS.
- `seek_step` | example: `5` | default: 1 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.

### silence.split_on_silence()

Returns list of audio segments from splitting audio_segment on silent sections.

**Supported keyword arguments**:

- `min_silence_len` | example: `500` | default: 1000 The minimum length for silent sections in milliseconds. If it is greater than the length of the audio segment an empty list will be returned.
- `silence_thresh` | example: `-20` | default: -16 The upper bound for how quiet is silent in dBFS.
- `seek_step` | example: `5` | default: 1 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.
- `keep_silence` ~ example: True | default: 100 How much silence to keep in ms or a bool. leave some silence at the beginning and end of the chunks. Keeps the sound from sounding like it is abruptly cut off. When the length of the silence is less than the keep_silence duration it is split evenly between the preceding and following non-silent segments. If True is specified, all the silence is kept, if False none is kept.

### silence.detect_leading_silence()

Returns the millisecond/index that the leading silence ends. If there is no end it will return the length of the audio_segment.

```
from pydub import AudioSegment, silence

print(silence.detect_silence(AudioSegment.silent(2000)))
# 2000
```

**Supported keyword arguments**:

- `silence_thresh` | example: `-20` | default: -50 The upper bound for how quiet is silent in dBFS.
- `chunk_size` | example: `5` | default: 10 Size of the step for checking for silence in milliseconds. Smaller is more precise. Must be a positive whole number.

## 其他

### AudioSegment(…).export()

将 `AudioSegment` 对象写入文件 – 返回输出文件的文件句柄（不过，您不必对其执行任何操作）。

```
from pydub import AudioSegment
sound = AudioSegment.from_file("/path/to/sound.wav", format="wav")

# simple export
file_handle = sound.export("/path/to/output.mp3", format="mp3")

# more complex export
file_handle = sound.export("/path/to/output.mp3",
                           format="mp3",
                           bitrate="192k",
                           tags={"album": "The Bends", "artist": "Radiohead"},
                           cover="/path/to/albumcovers/radioheadthebends.jpg")

# split sound in 5-second slices and export
for i, chunk in enumerate(sound[::5000]):
  with open("sound-%s.mp3" % i, "wb") as f:
    chunk.export(f, format="mp3")
```

第一个参数是写入输出的位置， **或** 要写入的文件句柄。如果不传递输出文件或路径，将生成一个临时文件。

**支持的关键字参数**:

- `format` | 例： `"aif"` | 默认： `"mp3"` 输出文件的格式。 支持 `"wav"` 和 `"raw"` , 所有其他格式都需要ffmpeg。
- `codec` | 例： `"libvorbis"` 对于可能包含使用不同编解码器编码的内容的格式，可以指定希望编码器使用的编解码器。例如，“ogg”格式通常与“libvorbis”编解码器一起使用。（需要ffmpeg）
- `bitrate` | 例： `"128k"` 对于压缩格式，可以传递希望编码器使用的比特率（需要ffmpeg）。每个编解码器都接受不同的比特率参数，因此请查看 [ffmpeg documentation](https://www.ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders) 以获取详细信息 (比特率通常显示为 `-b`, `-ba` or `-a:b`).
- `tags` | example: `{"album": "1989", "artist": "Taylor Swift"}` Allows you to supply media info tags for the encoder (requires ffmpeg). Not all formats can receive tags (mp3 can).
- `parameters` | 例： `["-ac", "2"]` Pass additional [command line parameters](https://www.ffmpeg.org/ffmpeg.html) to the ffmpeg call. These are added to the end of the call (in the output file section).
- `id3v2_version` | example: `"3"` | default: `"4"` Set the ID3v2 version used by ffmpeg to add tags to the output file. If you want Windows Exlorer to display tags, use `"3"` here ([source](http://superuser.com/a/453133)).
- `cover` | example: `"/path/to/imgfile.png"` Allows you to supply a cover image (path to the image file). Currently, only MP3 files allow this keyword argument. Cover image must be a jpeg, png, bmp, or tiff file.



### AudioSegment(…).export()

Write the `AudioSegment` object to a file – returns a file handle of the output file (you don't have to do anything with it, though).

```
from pydub import AudioSegment
sound = AudioSegment.from_file("/path/to/sound.wav", format="wav")

# simple export
file_handle = sound.export("/path/to/output.mp3", format="mp3")

# more complex export
file_handle = sound.export("/path/to/output.mp3",
                           format="mp3",
                           bitrate="192k",
                           tags={"album": "The Bends", "artist": "Radiohead"},
                           cover="/path/to/albumcovers/radioheadthebends.jpg")

# split sound in 5-second slices and export
for i, chunk in enumerate(sound[::5000]):
  with open("sound-%s.mp3" % i, "wb") as f:
    chunk.export(f, format="mp3")
```

The first argument is the location (as a string) to write the output, **or** a file handle to write to. If you do not pass an output file or path, a temporary file is generated.

**Supported keyword arguments**:

- `format` | example: `"aif"` | default: `"mp3"` Format of the output file. Supports `"wav"` and `"raw"` natively, requires ffmpeg for all other formats.
- `codec` | example: `"libvorbis"` For formats that may contain content encoded with different codecs, you can specify the codec you'd like the encoder to use. For example, the "ogg" format is often used with the "libvorbis" codec. (requires ffmpeg)
- `bitrate` | example: `"128k"` For compressed formats, you can pass the bitrate you'd like the encoder to use (requires ffmpeg). Each codec accepts different bitrate arguments so take a look at the [ffmpeg documentation](https://www.ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders) for details (bitrate usually shown as `-b`, `-ba` or `-a:b`).
- `tags` | example: `{"album": "1989", "artist": "Taylor Swift"}` Allows you to supply media info tags for the encoder (requires ffmpeg). Not all formats can receive tags (mp3 can).
- `parameters` | example: `["-ac", "2"]` Pass additional [command line parameters](https://www.ffmpeg.org/ffmpeg.html) to the ffmpeg call. These are added to the end of the call (in the output file section).
- `id3v2_version` | example: `"3"` | default: `"4"` Set the ID3v2 version used by ffmpeg to add tags to the output file. If you want Windows Exlorer to display tags, use `"3"` here ([source](http://superuser.com/a/453133)).
- `cover` | example: `"/path/to/imgfile.png"` Allows you to supply a cover image (path to the image file). Currently, only MP3 files allow this keyword argument. Cover image must be a jpeg, png, bmp, or tiff file.