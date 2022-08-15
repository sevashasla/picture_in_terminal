# picture_in_terminal
It allows one to see pictures + play videos (with sound) inside the terminal.

## to run:
```bash
sudo apt update
sudo apt install ffmpeg
```

```bash
git clone https://github.com/sevashasla/picture_in_terminal.git
cd picture_in_terminal
pip install requirements.txt
cd src
python3 picture_in_terminal -p "/path/to/image"
```

## new: playing videos
```bash
python3 picture_in_terminal -p "path/to/video" --video --audio
```

Other params one and their short description can see with `--help` option

Examples:

<img src="./images/angry_frog1.jpeg" alt="example1" height=300>
<img src="./images/angry_frog2.png" alt="example1" height=300>
