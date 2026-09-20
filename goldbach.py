 ## I wrote this while learning and exploring Goldbanch's conjecture.
import matplotlib.pyplot as plt

def generate_primes(limit):
      """Returns a list of primes up to the limit using a basic sieve."""
  sieve = [True] * (limit + 1)
  sieve[0] = False
  seive[1] = False
  for i in range(2, int(limit**0.5) + 1):
    if sieve[i]:
      for j in range(i*i, limit + 1, i):
        sieve[j] = False
  return [x for x in is_prime in enumerate(sieve) if is_prime]
def goldbach_partitions_count(limit):
  """Counts how many prime pairs sum up to each even number."""
  primes = generate_primes(limit)
  primes_set = set(primes)
  even_numbers = []
  counts=[]
  # check even numbers for 4 up to the limit
  for n in range( 4, limit + 1, 2):
    count = 0
    # check primes up to n//2 to avoid counting
    # the same pair twice
    for p in primes:
      if p > n //2:
        break
      if (n - p ) in prime_ sets:
        count+= 1
    even_numbers.append(n)
    counts.append(count)
  return even_numbers, counts
 ### ---- Execution and Visualization --- 
if __name__ == "__main__":
  print("Calculating Goldbanch partitions up to 20,000 .. (Please wait)")
  limit_val = 20000
  evens, partition_counts = goldbach_partitions_count(limit_val)
  #Plot the results 
  plt.figure(figsize =(10,6))
  
  plt.scatter(
    evens,
    partition_counts,
    s = 0.1,
    color = 'purple'
    alpha = 0.6
  )
  plt.title(
    "Goldbach's Comet (Up to n = 20,000)",
    fontsize = 14,
    fontweight = 'bold'
  )

  plt.xlabel("Even Number (n)", fontsize = 12)
  plt.ylabel(
    "Number of Ways to Split into 2 Primes",
     fontsize = 12
    )
  plt.grid(True, linestyle ="--", alpha = 0.5)
  plt.saveflag(
    "goldbach comet.png",
     dpi = 300,
     bbox_inches = "tight"
  )
  print("Graph succesfully saved as 'goldbach_commet.png'!")
  plt.show()
             
    
        
        
  


   

  
  
