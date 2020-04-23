import csv


def csv_upload(csv_file, KlassModel):
    file_data = csv_file.read()
    reader = csv.reader(file_data.decode("utf-8").replace(u'\ufeff', '').split('\r\n'))
    headers = next(reader, None)
    headers = [header for header in headers if header != '']
    print(headers)
    for row in reader:
        if not row or row[0].strip() == '':
            continue
        header_map = {header:row[ind] for ind, header in enumerate(headers)}
        KlassModel.objects.get_or_create(**header_map)
