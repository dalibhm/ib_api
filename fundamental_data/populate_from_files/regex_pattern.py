

re_pattern = os.path.join(cls.base_directory, '{}_{}_(.*).xml'.format(symbol, report_type))
regex = re.compile(pattern)
dates_str = [regex.search(file).group(1) for file in files]