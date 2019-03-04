import json
import argparse

from logging_config import logger
from create_doc import create_doc


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--json_file', type=str)
    args = parser.parse_args()
    return args


def main(args):
    logger.info(args)
    with open(args.json_file, 'r') as fin:
        json_dict = json.load(fin)
        items = json_dict['items']
        for item in items:
            summary = item['summary']
            if 'Seminar' not in summary:
                logger.warning(summary)
            else:
                logger.info(summary)
                location = item['location']
                start_time = item['start']['dateTime'] if 'dateTime' in item['start'] else item['start']
                end_time = item['end']['dateTime'] if 'dateTime' in item['end'] else item['end']
                summary = summary[10:]
                speecher, title, _ = summary.split('"')
                speecher = speecher[:-2]
                print(f"講題：{title}")
                print(f"講員：{speecher}")
                time = f"{start_time[:16].replace('T', ' ')} - {end_time[11:16]}"
                print(f"時間：{time}")
                print(f"地點：{location}")
                create_doc((time + title).replace(' ', '_'), title, speecher, time, location)


if __name__ == "__main__":
    args = parse_args()
    main(args)
