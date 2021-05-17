# Anime2Sketch
*Anime2Sketch: A sketch extractor for illustration, anime art, manga*

By [Xiaoyu Xiang](https://engineering.purdue.edu/people/xiaoyu.xiang.1)

![teaser demo](demos/vinland_saga.gif)

## Introduction
The repository contains the testing codes and pretrained weights for Anime2Sketch. Slightly modified by bycloud for Windows installation.

Anime2Sketch is a sketch extractor that works well on illustration, anime art, and manga. It is an application based on the paper ["Adversarial Open Domain Adaption for Sketch-to-Photo Synthesis"](https://arxiv.org/abs/2104.05703).

## Requirements
Anaconda3 Prompt is used

You can get it [here](https://www.anaconda.com/products/individual)

Or you can run it from Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shandytp/Anime2Sketch-Windows/blob/master/Anime2Sketch.ipynb)

## Get Started
### Installation 
```
conda create -n a2s python=3.6

conda activate a2s

conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
```
or if you are using NVIDIA 30 series
```
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
```

### Download Pretrained Weights
Please download the weights from [GoogleDrive](https://drive.google.com/drive/folders/1Srf-WYUixK0wiUddc9y3pNKHHno5PN6R?usp=sharing), and put it into the [weights/](weights/) folder.

### Test
```Shell
python test.py --dataroot /your_input/dir --load_size 512 --output_dir /your_output/dir
```
The above command includes three arguments:
- dataroot: your test file or directory
- load_size: due to the memory limit, we need to resize the input image before processing. By default, we resize it to `512x512`.
- output_dir: path of the output directory

## Run our example on a specific image:
```Shell
python test.py --dataroot test_samples/madoka.jpg --load_size 512 --output_dir results/
```
## or running on a folder:
```
python test.py --dataroot test_samples/*FOLDER_NAME* --load_size 512 --output_dir results/
```

## or running on a video:

Get ffmpeg
```
conda install -c conda-forge ffmpeg
```
We would need to extract all the frames first. Find out the FPS of the video by right clicking it. Drag the video into `test_samples` folder, and create the folder based on the mp4's name for ease use later.
```
ffmpeg -i test_samples/*YOUR_MP4_NAME*.mp4 -vf fps=*YOUR_FPS_COUNT* test_samples/*YOUR_MP4_NAME*/%06d.jpg
```
Run the main module:
```
python test.py --dataroot test_samples/*FOLDER_NAME* --load_size 512 --output_dir results/*FOLDER_NAME*
```
Put the images back together:
```
ffmpeg -i results/*YOUR_MP4_NAME*/%06d.jpg -vf fps=*YOUR_FPS_COUNT* results/*YOUR_MP4_NAME*.mp4
```

### Train
Check the main repository for more info

## More Results
Our model works well on illustration arts:
![madoka demo](demos/madoka_in_out.png)
![demo1](demos/demo1_in_out.png)
Turn handrawn photos to clean linearts:
![demo2](demos/demo2_in_out.png)
Simplify freehand sketches:
![demo3](demos/demo3_in_out.png)
And more anime results:
![demo4](demos/vinland_3.gif)
![demo5](demos/vinland_1.gif)


## License
This project is released under the [MIT License](LICENSE).

## Citations
```BibTex
@misc{Anime2Sketch,
  author = {Xiaoyu Xiang, Ding Liu, Xiao Yang, Yiheng Zhu, Xiaohui Shen},
  title = {Anime2Sketch: A Sketch Extractor for Anime Arts with Deep Networks},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Mukosame/Anime2Sketch}}
}

@misc{xiang2021adversarial,
      title={Adversarial Open Domain Adaption for Sketch-to-Photo Synthesis}, 
      author={Xiang, Xiaoyu and Liu, Ding and Yang, Xiao and Zhu, Yiheng and Shen, Xiaohui and Allebach, Jan P},
      year={2021},
      eprint={2104.05703},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
