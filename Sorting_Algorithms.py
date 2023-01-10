import time
import random

cmp = 0
TYPE = 0


def algochooser(numbers, paint, label_comparison, something, TYPE_OF_DRAW, speed):
    global cmp, TYPE
    TYPE = TYPE_OF_DRAW

    if something == "Insertion Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        insertionsort(numbers, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Merge Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        mergesort(numbers, 0, len(numbers), paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0


def insertionsort(number, paint, label_comparison, speed):
    global cmp, TYPE
    colors = []
    for i in range(1, len(number)):
        current = number[i]
        y = i - 1
        while (y >= 0 and number[y] > current):
            number[y + 1] = number[y]
            y -= 1
            cmp += 1
            # ----------------------------------------------------------
            if TYPE == 0:
                for gh in range(len(number)):
                    if y == gh:
                        colors.append("#cc0000")
                    elif gh == i:
                        colors.append("green")
                    else:
                        colors.append("antique white")
            else:
                colors = [((int)(x * 360) / 950) for x in number]
            time.sleep(1 / speed)
            paint(colors)
            colors = []
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
            # ------------------------------------------------------------
        number[y + 1] = current
        cmp += 1
        # -----------------------------------------------------------
        label_comparison.configure(text="No. of comparisons: " + str(cmp))


def mergesort(number, left, right, paint, label_comparison, speed):
    if left < right:
        middle = (left + right) // 2
        mergesort(number, left, middle, paint, label_comparison, speed)
        mergesort(number, middle + 1, right, paint, label_comparison, speed)
        merge(number, left, middle, right, paint, label_comparison, speed)


def merge(number, left, middle, right, paint, label_comparison, speed):
    global cmp, TYPE
    si = fi = 0
    colors = []
    firstlist = number[left:middle + 1]
    secondlist = number[middle + 1:right + 1]
    for ai in range(left, right + 1):
        if (fi < len(firstlist) and si < len(secondlist)):
            if (firstlist[fi] < secondlist[si]):
                number[ai] = firstlist[fi]
                fi += 1
                cmp += 1
            else:
                number[ai] = secondlist[si]
                si += 1
        elif (fi < len(firstlist)):
            number[ai] = firstlist[fi]
            fi += 1
        elif (si < len(secondlist)):
            number[ai] = secondlist[si]
            si += 1
        if TYPE == 0:
            for x in range(len(number)):
                if x > middle and x <= right:
                    colors.append("yellow")
                elif x >= left and x <= middle:
                    colors.append("teal")
                else:
                    colors.append("antique white")
        else:
            colors = [((int)(x * 360) / 950) for x in number]
        paint(colors)
        time.sleep(1 / speed)
        label_comparison.configure(text="No. of comparisons: " + str(cmp))