import sys
print(sys.version)
records = redshift_hook.get_records(f"SELECT COUNT(*) FROM {self.table};")