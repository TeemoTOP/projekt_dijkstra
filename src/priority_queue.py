# src/priority_queue.py

class PriorityQueue:
    def __init__(self):
        """
        Inicjalizuje pustą kolejkę priorytetową opartą na kopcu binarnym.
        """
        self.heap = []

    def push(self, item, priority):
        """
        Dodaje element do kolejki priorytetowej.

        :param item: Element do dodania
        :param priority: Priorytet elementu
        """
        self.heap.append((priority, item))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """
        Usuwa i zwraca element o najwyższym priorytecie (najniższa wartość).

        :return: Tuple (element, priorytet)
        """
        if not self.heap:
            raise IndexError("Pop from empty priority queue")
        self._swap(0, len(self.heap) - 1)
        priority, item = self.heap.pop()
        self._heapify_down(0)
        return item, priority

    def is_empty(self):
        """
        Sprawdza, czy kolejka jest pusta.

        :return: True jeśli pusta, False w przeciwnym razie
        """
        return len(self.heap) == 0

    def _heapify_up(self, index):
        """
        Przeprowadza operację heapify up od podanego indeksu.

        :param index: Indeks elementu do przesunięcia w górę
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """
        Przeprowadza operację heapify down od podanego indeksu.

        :param index: Indeks elementu do przesunięcia w dół
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        """
        Zamienia miejscami dwa elementy w kopcu.

        :param i: Indeks pierwszego elementu
        :param j: Indeks drugiego elementu
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
