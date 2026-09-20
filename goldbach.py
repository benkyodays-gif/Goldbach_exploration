 ## I wrote this while learning and exploring Goldbach's conjecture.
import matplotlib.pyplot as plt


def generate_primes(limit):
    """Return a list of primes up to the given limit using a basic sieve."""
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [x for x, is_prime in enumerate(sieve) if is_prime]


def goldbach_partitions_count(limit):
    """Count how many prime pairs sum to each even number."""
    primes = generate_primes(limit)
    primes_set = set(primes)
    even_numbers = []
    counts = []

    for n in range(4, limit + 1, 2):
        count = 0
        for p in primes:
            if p > n // 2:
                break
            if (n - p) in primes_set:
                count += 1
        even_numbers.append(n)
        counts.append(count)

    return even_numbers, counts


# ---- Execution and Visualization ---
if __name__ == "__main__":
    print("Calculating Goldbach partitions up to 20,000 .. (Please wait)")
    limit_val = 20000
    evens, partition_counts = goldbach_partitions_count(limit_val)

    plt.figure(figsize=(10, 6))
    plt.scatter(
        evens,
        partition_counts,
        s=0.1,
        color="purple",
        alpha=0.6,
    )
    plt.title(
        "Goldbach's Comet (Up to n = 20,000)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Even Number (n)", fontsize=12)
    plt.ylabel("Number of Ways to Split into 2 Primes", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig("goldbach_comet.png", dpi=300, bbox_inches="tight")
    print("Graph successfully saved as 'goldbach_comet.png'!")
    plt.show()
             
    
        
        
  


   

  
  