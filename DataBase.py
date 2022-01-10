import json




class json_eidit:
    def add(from_, new_line):
        # opening file as f
        with open("data.json") as f:
            data = json.load(f)

        # geting data of from_ and converting it to list
        _from = list(data[from_])


        # appending new_line to _from
        _from.append(new_line)

        # getinting _from from the data and exchinging with
        data[from_] = _from

        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
    


    def remove(from_, dic_of):
        # opening file as f

        with open("data.json") as f:
            data = json.load(f)

        # geting data of from_ and converting it to list
        _from = list(data[from_])


        # removing new_line to _from
        _from.remove(dic_of)

        # getinting _from from the data and exchinging with
        data[from_] = _from


        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
    
    def get_all_in(from_):
        # opening file as f
        try:
            with open("data.json") as f:
                data = json.load(f)
                _from = data[from_]
        except:
            templat = {
                "todo":[
                ],
                "complet_todo":[

                ]
            }
            with open("data.json", "w") as n:
                json.dump(templat, n, indent=2)
            _from = None

        return _from

if __name__ == "__main__":
    s = json_eidit.get_all_in("todo")
    print(s)
