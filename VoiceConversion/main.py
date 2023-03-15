import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--src_wav', type=str, help='the wav file to conversion')
    parser.add_argument('--trg_spk', type=str, help='who is target spk.')

    config = parser.parse_args()
    
    print(config)
    if config.src_wav is None:
        raise RuntimeError("Please enter the source wav file path which want to convert.")
    if config.trg_spk is None:
        raise RuntimeError("Please enter the target wav file path which want to convert.")

    print(config.src_wav , config.trg_spk)    

# python main.py --src_wav 2 --trg_spk 2