#Zaimplementowac algorytm Aho-Corasick
#zad 4

from collections import deque, defaultdict


class AhoCorasick:
    def __init__(self, words):
        # Trójka (trie, fail, output)
        self.num_nodes = 1
        self.edges = [{}]  # Krawędzie
        self.fail = [-1]  # Fail links (linki do najbardziej podobnych prefiksów)
        self.output = [[]]  # Lista wyników dla każdego węzła

        # Dodajemy wszystkie słowa do drzewa (trie)
        for word in words:
            self.add_word(word)

        # Ustalamy fail links
        self.build_fail_links()

    def add_word(self, word):
        current_node = 0
        for letter in word:
            if letter not in self.edges[current_node]:
                self.edges[current_node][letter] = self.num_nodes
                self.edges.append({})
                self.fail.append(-1)
                self.output.append([])
                self.num_nodes += 1
            current_node = self.edges[current_node][letter]
        self.output[current_node].append(word)

    def build_fail_links(self):
        queue = deque()

        # Inicjujemy węzły 1-ego poziomu
        for letter in range(256):  #256 znaków ASCII
            letter = chr(letter)
            if letter in self.edges[0]:
                self.fail[self.edges[0][letter]] = 0
                queue.append(self.edges[0][letter])
            else:
                self.edges[0][letter] = 0

        # Ustalamy fail links dla wszystkich węzłów
        while queue:
            current_node = queue.popleft()

            for letter, next_node in self.edges[current_node].items():
                # Wyszukujemy fail link dla next_node
                fail_state = self.fail[current_node]
                while letter not in self.edges[fail_state]:
                    fail_state = self.fail[fail_state]
                fail_state = self.edges[fail_state][letter]
                self.fail[next_node] = fail_state
                self.output[next_node].extend(self.output[fail_state])
                queue.append(next_node)

    def search(self, text):
        current_node = 0
        results = []
        for i in range(len(text)):
            letter = text[i]

            # Idziemy po krawędziach (jeśli nie ma krawędzi, to podążamy po fail linku)
            while letter not in self.edges[current_node]:
                current_node = self.fail[current_node]

            current_node = self.edges[current_node][letter]

            # Jeśli w węźle mamy jakieś słowa, to zapiszemy wynik
            if self.output[current_node]:
                for word in self.output[current_node]:
                    results.append((i - len(word) + 1, word))

        return results


# Przykładowe użycie:
words = ["he", "she", "his", "hers"]
text = "ushers"

aho_corasick = AhoCorasick(words)
result = aho_corasick.search(text)

# Wypisanie wyników
print("Wyniki wyszukiwania:")
for start_index, word in result:
    print(f"Znaleziono słowo '{word}' na pozycji {start_index}")


