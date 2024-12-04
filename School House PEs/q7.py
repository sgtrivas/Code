file_results= "10.50.1.200:990"
scan_result=dict()
scan_result["IP_ADDRESS"] = file_results.split(":")[0]
scan_result["LISTENING_PORT"] = file_results.split(":")[1]


port = scan_result.pop("LISTENING_PORT")
print(f"""{scan_result.get("IP_ADDRESS"):}\t{port}""")