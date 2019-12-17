import yaml
from itertools import groupby

def main():
    with open('short.yaml') as file:
        yml = yaml.load(file, Loader=yaml.BaseLoader)

    images = yml['MonoBehaviour']['m_Images']
    good_images = [i for i in images if int(i['Quality']) > 70]
    sorted_good_images = sorted(good_images, key = lambda i: i['Quality'], reverse=True)

    for score, items in groupby(sorted_good_images, key = lambda i: i['Quality']):
        print(score)
        for i in items:
            print(f"{i['Name']}.jpg")
        print('')

if __name__ == "__main__":
    main()
