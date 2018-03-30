def psychologist():
    response = "So, let's begin!"
    while True:
        question = yield response
        if question is None:
            response = "what?"
        if question.endswith("?"):
            response = "don't ask yourself too much question!"

p = psychologist()
print(next(p))
print(p.send("what?"))
