import argparse
from serializers.factory import Factory

def main():
    parser = argparse.ArgumentParser(description='Input files to format')
    parser.add_argument('input', type=str, help='File for load')
    parser.add_argument('output', type=str, help='File for dump')
    args = parser.parse_args()
    data = Factory.create_serializer(args.input[-4:]).load(args.input)
    Factory.create_serializer(args.output[-4:]).dump(data, args.output)

if __name__ == '__main__':
    main()