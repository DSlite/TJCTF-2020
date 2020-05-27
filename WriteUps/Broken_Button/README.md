# Broken Button - 10 points - Web

## Description

This [site](http://broken_button.tjctf.org/) is telling me all I need to do is click a button to find the flag! Is it really that easy?

## Solution

Pada tampilan awal website terdapat sebuah button yang tidak dapat di klik. Ketika saya inspect element terhadap button tersebut, ternyata attribute `href` menunjuk pada sebuah alamat.

![inspect](./inspect.png)

Alamat tersebut saya buka dan muncul flagnya.

![flag](./flag.png)

## Flag

```
tjctf{wHa1_A_Gr8_1nsp3ct0r!}
```