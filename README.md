# ocvsee

Program to create chains of OpenCV functions.

Very unstable. Will crash on any non valid input. May freeze after close OpenCV window.

## Example

### Original image:

![](https://i.imgur.com/opdQ2ll.png)

### Program:

![](https://i.imgur.com/dGxb8Hr.png)

Which, in terms of code, equal to:

```python
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                               
image = cv2.blur(image, ksize=(7, 7))
image = cv2.threshold(image, 110, 255, cv2.THRESH_BINARY)[1]
```
