"""
Wimbledon
Estimate: 30 minutes
Actual:   40 minutes
"""
FILENAME = "wimbledon.csv"


def main():
    """Load the .csv file, process its contents, and print final results"""
    unprocessed_data = load_wimbledon_data()
    winner_to_wins, winning_countries = process_wimbledon_data(unprocessed_data)
    display_wimbledon_results(winner_to_wins, winning_countries)


def load_wimbledon_data():
    """Open the .csv file and save the unprocessed content before closing"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        unprocessed_data = in_file.readlines()
    return unprocessed_data


def process_wimbledon_data(unprocessed_data):
    """Process the Wimbledon data, returning a dictionary for winners and set for countries"""
    winner_to_wins = {}
    wimbledon_data = [line.split(",") for line in unprocessed_data]
    for match_data in wimbledon_data[1:]:
        winner = match_data[2]
        if winner in winner_to_wins:
            winner_to_wins[winner] += 1
        else:
            winner_to_wins[winner] = 1
    winning_countries = {match_data[1] for match_data in wimbledon_data[1:]}
    return winner_to_wins, winning_countries


def display_wimbledon_results(winner_to_wins, winning_countries):
    """Display final results by printing every winner and their scores, and all winning countries"""
    for winner, number_of_wins in winner_to_wins.items():
        print(winner, number_of_wins)
    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


main()
