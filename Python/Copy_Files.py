#!/usr/bin/python3

"""
Author:   Benjamin Parry
Blog:     benjamin.parry.com
Post:     ...
Link:     http://benjamin-parry.com/...
"""

import os
import shutil

frame_dir = r"Z:\Project_Media\Nestle\H111588_Purina\B114118_Purina_GPS\Vfx" \
            r"\PC010\3D\maya\sourceimages\benparry\Cat_Key_Rough_Matte"

suffix = "exr"
start_frame = 940

files_in_dir = os.listdir(frame_dir)

frame_split = os.path.splitext(files_in_dir[0])

frames = sorted([f for f in files_in_dir
                 if os.path.splitext(f)[1][1:] == suffix])

file_base_name = ("".join(frames[0].split(".")[:-2])) + "."

frame_numbers = [f.split(".")[1] for f in frames]

new_frames = [os.path.join(frame_dir,
                           (file_base_name + str(i).zfill(4) + "." + suffix))
              for i in range(start_frame, int(frame_numbers[0]))]

first_frame = os.path.join(frame_dir, frames[0])


def copy_frames():
    for frame in new_frames:
        shutil.copy2(first_frame, frame)

copy_frames()

# print(files_in_dir)
print(first_frame)
print(file_base_name)
# print(frame_split)
# print(frame_numbers)
print(frame_numbers[0] + " > " + frame_numbers[-1])
print(new_frames)
