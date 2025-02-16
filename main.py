from os import path
from argparse import ArgumentParser
from config import default_output_file_name
from core.model.garmin_activity import GarminActivity


def parse_arguments():
    argument_parser = ArgumentParser("Fitness Activity Parser", add_help=False)

    argument_parser.add_argument("--file", action="store", help="Path to origin file for parsing. Formats accepted: [.tcx, .gpx]")
    argument_parser.add_argument("--output", action="store", help="Path to destin file for writing. Writing format will be Json.")
    argument_parser.add_argument("-h", "--help", action="help", help="Show this message and leaves.")

    return argument_parser.parse_args()

def main() :
    arguments = parse_arguments()
    if arguments.file :
        garmin_activity = GarminActivity(arguments.file).parse()
        if arguments.output :
            if path.isdir(arguments.output):
                with open(path.join(arguments.output, default_output_file_name), 'w') as file_to_write:
                    file_to_write.write(garmin_activity.to_json())
            elif path.isfile(arguments.output):
                raise FileExistsError
            else:
                raise 'Could not open file'
        else :
            print(garmin_activity.to_json())
    else :
        print('Missing file argument.')

if __name__ == '__main__':
    main()