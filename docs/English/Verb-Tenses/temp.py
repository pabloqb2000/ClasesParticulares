import json

with open("data.temp", "r") as f:
    data_str = f.read()

    tenses = data_str.split('\n\n\n')
    tenses_data = []
    print("TENSES:", len(tenses))
    for tense in tenses:
        tense_data = tense.split('\n\n')
        title, signal_words, use, form, examples = tense_data
        print(title)

        signal_words = signal_words.split('\n')
        use = use.split('\n')
        form = form.split('\n')
        examples = examples.split('\n')

        signal_words = signal_words if signal_words != ["Null"] else []

        tenses_data.append({
            "name": title,
            "signal words": signal_words,
            "use": use,
            "form": form,
            "p1-r-pos": examples[0],
            "p1-r-neg": examples[1],
            "p1-r-int": examples[2],
            "p3-r-pos": examples[3],
            "p3-r-neg": examples[4],
            "p3-r-int": examples[5],
            "p1-ir-pos": examples[6],
            "p1-ir-neg": examples[7],
            "p1-ir-int": examples[8],
            "p3-ir-pos": examples[9],
            "p3-ir-neg": examples[10],
            "p3-ir-int": examples[11],
        })

with open("app_data.json", "w+") as f:
    json.dump({"data": tenses_data}, f, indent=2)
