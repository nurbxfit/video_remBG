# Aout

Simple script demo, on how to remove background from a video.
It take a video, extract it frames into images, apply background removal and then stitch it back together into a new video.

# (about branch) dev/http-server

Added simple REST API server, we can upload video, and it will automatically process the video
Currently we not blocking the request, we immediately return a response while the video being processed in background via multi thereading.

Note:

- rembg, already have start as server features using the `s` options or using the `docker` version [refer here](https://github.com/danielgatis/rembg#rembg-s),
- Here I just learning to create my own server.

If u want to start the existing rembg server using docker, can refer the command below

```
docker run -p 7000:7000 --name my_rembg_container danielgatis/rembg s --host 0.0.0.0 --port 7000 --log_level info
```

## TODO:

Because we are not blocking the request,
after the video process, we should do something to let know the sender, that the video finished processed.
Maybe we can assign the video with an id, later the sender can query the id to check if the video done processed or not.
Or maybe we can use websocekt or webhook (if sender from another server) to notified the sender that their video finished processing.

In future if we were to make it as final usable product,
we need to consider these cases:

- we should seperate the extracted folder for every incoming request
- we check the hash, if user send the same video, we can skip the extraction process
- we shall clear the folders regularly to reduce disk usage.
- we need to consider better model or better GPU to process removing the background.

(note: this repo is just a POC)

## Note:

- You might need to change the provider based on ur running machine, I run on an AMD ryzen laptop so I use the AMD GPU provider.
- you can refer the list here [Provider](https://onnxruntime.ai/docs/execution-providers/)

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
