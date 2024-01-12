import argparse
import os

import sofa
import soundfile as sf


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    parser.add_argument('output_dir')
    args = parser.parse_args()

    sofa_filenames = [
        'UniS_Room_A_BRIR_16k.sofa',
        'UniS_Room_B_BRIR_16k.sofa',
        'UniS_Room_C_BRIR_16k.sofa',
        'UniS_Room_D_BRIR_16k.sofa',
    ]

    output_subdirnames = [
        'Room_A/16kHz',
        'Room_B/16kHz',
        'Room_C/16kHz',
        'Room_D/16kHz',
    ]

    ss = [
        32,
        47,
        68,
        89,
    ]

    degs = [-90 + i*5 for i in range(37)]

    for sofa_filename, output_subdirname, s in zip(
        sofa_filenames,
        output_subdirnames,
        ss
    ):
        sofa_file = os.path.join(args.input_dir, sofa_filename)
        db = sofa.Database.open(sofa_file)
        brirs = db.Data.IR.get_values()
        output_subdir = os.path.join(args.output_dir, output_subdirname)
        os.makedirs(output_subdir, exist_ok=True)
        for i in range(brirs.shape[0]):
            output_file = os.path.join(
                output_subdir,
                f'CortexBRIR_0_{s}s_{degs[i]}deg_16k.wav',
            )
            sf.write(
                output_file,
                brirs[i, :, :].T,
                16000
            )
