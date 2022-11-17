import argparse
from datetime import datetime
from kohonen import apply_kohonen

def main():
    t_start = datetime.now()

    # Parse arguments
    parser = argparse.ArgumentParser(description="Kohonen Space Mapping")

    # Add arguments
    parser.add_argument('-n', dest='n_kohonen', required=True)  # Size of network
    parser.add_argument('-nd', dest='n_data', required=True)  # Size of data
    parser.add_argument('-it', dest='iterations', required=True)  # Kohonen iterations
    parser.add_argument('-fig', dest='fig', required=False)  # Figure to map
    parser.add_argument('-line', dest='line', action='store_true')  # Plots lines between Kohonen points

    args = parser.parse_args()

    n_kohonen = None 
    n_data = None 
    iterations = None
    fig = 'grid'
    line = args.line
    if args.n_kohonen != None:
        n_kohonen = int(args.n_kohonen)
    if args.iterations != None:
        iterations = int(args.iterations)
    if args.n_data != None:
        n_data = int(args.n_data)
    if args.fig != None:
        fig = args.fig

    apply_kohonen(n_kohonen, iterations, n_data, fig, line)
    t_end = datetime.now()

    delta = t_end - t_start
    print(f"Total execution: {delta.total_seconds()} seconds")


if __name__ == '__main__':
    main()
