// 390ms(78.31%), 96.7MB(10.84%)
class Heap {
  constructor(compareFn) {
    this.values = []

    this.compareFn = compareFn
  }

  compare(a, b) {
    const result = this.compareFn(a, b)
    if (typeof result === "boolean") {
      return result
    }
    return result < 0 ? true : false
  }

  get top() {
    return this.values.length > 0 ? this.values[0] : undefined
  }

  get size() {
    return this.values.length
  }

  add(element) {
    this.values.push(element)
    this.percolateUp(this.values.length - 1)
  }

  extract() {
    if (this.values.length < 1) {
      throw new Error("heap is empty")
    }

    const top = this.values[0]
    const end = this.values.pop()

    if (this.values.length > 0) {
      this.values[0] = end
      this.percolateDown(0)
    }

    // return the top
    return top
  }

  swap(aIndex, bIndex) {
    ;[this.values[aIndex], this.values[bIndex]] = [
      this.values[bIndex],
      this.values[aIndex],
    ]
  }

  parent(index) {
    return Math.floor(Math.floor((index - 1) / 2))
  }

  leftChild(index) {
    return index * 2 + 1
  }

  rightChild(index) {
    return index * 2 + 2
  }

  isLeaf(index) {
    return (
      index >= Math.floor(this.values.length / 2) &&
      index <= this.values.length - 1
    )
  }

  percolateUp(index) {
    let currentIndex = index
    let parentIndex = this.parent(currentIndex)

    while (
      currentIndex > 0 &&
      this.compare(this.values[currentIndex], this.values[parentIndex])
    ) {
      this.swap(currentIndex, parentIndex)
      currentIndex = parentIndex
      parentIndex = this.parent(parentIndex)
    }
  }

  percolateDown(index) {
    if (!this.isLeaf(index)) {
      let leftChildIndex = this.leftChild(index)
      let rightChildIndex = this.rightChild(index)
      let largestIndex = index

      if (
        this.compare(this.values[leftChildIndex], this.values[largestIndex])
      ) {
        largestIndex = leftChildIndex
      }

      if (
        this.compare(this.values[rightChildIndex], this.values[largestIndex])
      ) {
        largestIndex = rightChildIndex
      }

      if (largestIndex !== index) {
        this.swap(index, largestIndex)
        this.percolateDown(largestIndex)
      }
    }
  }
}

/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
var findMaximizedCapital = function (k, w, profits, capital) {
  const n = profits.length
  const projects = Array.from({ length: n }, (v, i) => i)
    .map((i) => [capital[i], profits[i]])
    .sort((a, b) => a[0] - b[0])

  let index = 0
  const maxHeap = new Heap((a, b) => b - a)

  const insertToHeap = () => {
    while (index < n) {
      const [cost, profit] = projects[index]
      if (cost <= w) {
        maxHeap.add(profit)
        index += 1
      } else {
        break
      }
    }
  }

  insertToHeap()

  while (k > 0 && maxHeap.size > 0) {
    w += maxHeap.extract()
    k -= 1
    insertToHeap()
  }

  return w
}
