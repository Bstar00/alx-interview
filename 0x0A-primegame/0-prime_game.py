#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(num_rounds, sets_of_integers):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        num_rounds (int): The number of rounds.
        sets_of_integers (list of int): A list of integers where each integer n
        denotes a set of consecutive integers starting from 1 up to and
        including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if num_rounds <= 0 or sets_of_integers is None:
        return None
    if num_rounds != len(sets_of_integers):
        return None

    # Initialize scores and an array to mark prime numbers
    ben_score = 0
    maria_score = 0

    # Create a list 'is_prime' of length max(sets_of_integers)
    # + 1 with all elements
    # initialized to 1
    is_prime = [1 for _ in range(max(sets_of_integers) + 1)]

    # Mark 0 and 1 as non-prime
    is_prime[0], is_prime[1] = 0, 0

    # Use Sieve of Eratosthenes algorithm to generate an array of prime numbers
    for i in range(2, len(is_prime)):
        remove_multiples_of_prime(is_prime, i)

    # Play each round of the game
    for max_integer in sets_of_integers:
        # If the sum of prime numbers in the set is even, Ben wins
        if sum(is_prime[0:max_integer + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    # Determine the winner of the game
    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    else:
        return None


def remove_multiples_of_prime(prime_list, prime_number):
    """
    Removes multiples of a prime number from a list of possible prime numbers.

    Args:
        prime_list (list of int): An array of possible prime numbers.
        prime_number (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # This loop iterates over multiples of a prime number and marks them as
    # non-prime by setting their corresponding value to 0 in the input
    # list prime_list. It starts from 2 and sets every multiple of prime_number
    # up to the length of prime_list to 0. If the index i * prime_number is
    # out of range for the list prime_list, it raises an IndexError exception,
    # and the loop terminates using the break statement.
    for i in range(2, len(prime_list)):
        try:
            prime_list[i * prime_number] = 0
        except (ValueError, IndexError):
            break
