num_of_english_subscribers = int(input())
english_subscribers = set(map(int, input().split()))

num_of_french_subscribers = int(input())
french_subscribers = set(map(int, input().split()))

print(len(english_subscribers.union(french_subscribers)))