# Linearithmic toset
This is an Anki add-on to help you memorise sequences by their order, without trying to recall the items themselves.
"Linearithmic" describes the quantities of cards.
"Toset" describes the structure of the sequences.
See Theory for details on both.

examples: streets, memory, operators

## Problem
Suppose you got sick of parentheses and type errors, so you want to learn operator precedence in full.
Naively, to memorise a list like that, you might make associations (cards) from each item to the next.

> Q: `a.b`, `a[i]`, `a++`, next lower precedence?
>
> A: `-a`, `~a`, `(T)a`

> Q: `-a`, `~a`, `(T)a`, next lower precedence?
>
> A: `a*b`, `a/b`, `a%b`

> Q: `a*b`, `a/b`, `a%b`, next lower precedence?
>
> A: `a+b`, `a-b`

It's easy enough to make cards like in bulk, such as with Yukogurafu.
But if you study like this, you run into some trouble.

In practice, you'll see from context whatever items have to care about.
You write code and can already see that you're using (say) `&`, `==`, `<<`, and `+` operators.
Explicitly recalling what the items in the list are is a waste of effort.

If you never use `^`, which is between `&` and `|`, you'll tend to forget that `^` follows `&` and that `|` follows `^`.
That makes your knowledge of important items fragile, dependent on their position relative to unimportant items.

If you switch to another version of the list that inserts or removes entries, you'll repeatedly mess up when reviewing the card that goes over that stretched gap.
JavaScript introduces `a**b` between `-a` and `a*b`.
If you then go back to your cards designed for C that ask about `-a` and `a*b`, you'll fail the card when you recall `a**b`.
Or vice versa: you program in C, then come back to JavaScript cards, and forget `a**b`.
In either case, you may still know correctly that the order of operations is `-a`, `a**b`, then `a*b`.
But the cards won't show that.

None of this is unique to operator precedence.
| The list is ... | ... but what you need to know is ... | ... and you might or might not include |
|-----------------|--------------------------------------|---------------------------------------|
| `a++`, `-a`, `a*b`, `a+b` | which of a pair binds more tightly? | `a**b` |
| Birch Ave, Maple Rd, Oak St | should you go E or W? | Spruce Alley |
| registers, CPU cache, RAM, disk | which is faster? | NVRAM |

## Theory
An ordered list is a toset: a set of objects under a [total order]( https://en.wikipedia.org/wiki/Total_order ).
Abstract away the objects, and what you have left is a comparison operator: a decision of which item comes first, given any two items.
If what you need to know is the order, what you should study is the set of those decisions.

> Q: `-a`, `~a`, `(T)a` to `a+b`, `a-b`, which way?
>
> A: lower precedence

On a set of $n$ elements, there are $n (n - 1)$ such decisions to learn.
This is $O(n^2)$ or, colloquially, too much.

That figure assumes you compare each item to each other item.
Instead, compare each item to items exponentially away, in each direction.
For example, from item 6 on a list, you make cards that compare it to items 2, 4, 5, 7, 8, 10, 14, with respective distances 4, 2, 1, 1, 2, 4, 8.
This way, you learn to put items close together in the right order, and you learn connections in the order between distant items, to help tie the whole list together.

That strategy gives a number of cards linearithmic ($O(n \log{n})$) to the number of elements, which is more manageable.

## Setup
Install it from AnkiWeb, when I post it there.
Until then, download the ZIP and install it manually with Anki's menu.
If needed, restart Anki.
If it still doesn't work, raise an issue here with the error message and/or faulty behaviour.

## Usage
Most features of linearithmic-toset are concentrated in "Edit Sequence Ordering", in the Tools menu at the top.
That menu entry launches a GUI.
If you start it with the note browser open, it will operate on whichever note is focused in the browser.
Otherwise, it will make and operate on a new note, its cards to go in the current deck.
