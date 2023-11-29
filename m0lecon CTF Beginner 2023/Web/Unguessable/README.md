# Unguessable

This challenge was the easiest in the CTF (it had __more solves than__ the sanity check, lol). In fact, to solve it, all you had to do was understand that the website fetched the flag from an endpoint `/vjfYkHzyZGJ4A7cPNutFeM/flag`, and to obtain it we ~~opened the endpoint~~ sniffed the whole network.

```javascript
...
function update(res) { // the function used by the site to get the flag
    if (res === "wrong") {
    card.style.backgroundColor = "red";
    text.innerText = "Wrong, try again";
    } else {
    card.style.backgroundColor = "green";
    fetch("/vjfYkHzyZGJ4A7cPNutFeM/flag")
        .then((response) => response.text())
        .then((str) => {
        text.innerText = str
        });
    }

    card.removeAttribute("hidden");
}
...
```

### Challenge Description
> You will never guess the number on this website!