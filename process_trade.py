from os import listdir, linesep
from os.path import isfile, join, basename
from lxml import html

import click
import pandas as pd


@click.command()
@click.option('--file_dir', default=r'.\tradeReport', help='Trade data input folder')
@click.option('--output_dir', default=r'.\tradeReport', help='Tick data output folder')
@click.option('--prefix', default='bryan', help='Prefix naming for excel output file')
def main(file_dir, output_dir, prefix):
    file_paths = [join(file_dir, f) for f in listdir(file_dir) if isfile(join(file_dir, f)) and '.html' in f]

    for file_path in file_paths:
        print('processing ' + file_path + '...')
        with open(file_path, 'r') as f:
            tree = html.fromstring(f.read().replace('\n', ''))
            account = tree.xpath('//*[@id="summaryDetailTable"]/tbody/tr[@class="row-summary no-details"]/td[1]/text()')
            tickers = tree.xpath('//*[@id="summaryDetailTable"]/tbody/tr[@class="row-summary no-details"]/td[2]/text()')
            trade_time = tree.xpath('//*[@id="summaryDetailTable"]/tbody/tr[@class="row-summary no-details"]/td[3]/text()')
            action = tree.xpath('//*[@id="summaryDetailTable"]/tbody/tr[@class="row-summary no-details"]/td[6]/text()')
            shares = tree.xpath('//*[@id="summaryDetailTable"]/tbody/tr[@class="row-summary no-details"]/td[7]/text()')
            price = tree.xpath('//*[@id="summaryDetailTable"]/tbody/tr[@class="row-summary no-details"]/td[8]/text()')
            print('hello')
            header = ','.join(['Instrument', 'Action','Type', 'Quantity', 'Limit', 'Stop','State', 'Filled',
                               'Avg. price', ' Remaining', 'Name', 'Strategy', 'OCO', 'TIF', 'Acoount display name',
                               'ID', 'Time', 'Cancel'])
            processed_file_name = join(output_dir, prefix+'_NT_' + basename(file_path)).replace('.html','.csv')
            with open(processed_file_name, 'a') as f1:
                f1.write(header + '\n')
                for i in range(0,len(account)):
                    line = '{0},{1},,{2},,,,,{3},,,,,,,,{4},'.format(tickers[i], action[i], shares[i], price[i], trade_time[i].replace(',',''))
                    f1.write(line + '\n')

if __name__ == '__main__':
    main()
