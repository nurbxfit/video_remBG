# Aout

Simple script demo, on how to remove background from a video.
It take a video, extract it frames into images, apply background removal and then stitch it back together into a new video.

# How to run (Windows)

1. cd into this directory

```
cd bgRemove
```

2. create new virtual environment

```
python3 -m venv .venv
```

3. get into the environment

```
 .\.venv\Scripts\activate
```

4. install dependencies

```
pip install -r .\requirements.txt
```

5. run the script

```
cd src && python main.py

```

6. get our of venv

```
deactivate
```
