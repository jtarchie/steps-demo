# steps-demo

A tiny pretend shop, so [steps](https://github.com/jtarchie/steps) pipelines have
something real to triage and review on camera. Nothing here is production code.

- `shop/cart.py`: subtotal, shipping, totals.
- `shop/slip.py`: the packing slip, which prints what each box cost to ship.
- `python3 -m unittest` runs the tests.

## The pipeline

[`review.yml`](review.yml) reviews every open pull request here and posts
only the bugs it can prove: the agent writes a failing test for each one, and
a separate step runs those tests before anything is posted.

```bash
brew tap jtarchie/steps https://github.com/jtarchie/steps
brew install --cask steps
steps run review.yml
```

It needs `GH_TOKEN`, Docker, and a model (the file's comments say which).
