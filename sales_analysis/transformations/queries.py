get_failed_files = '''select distinct file_name from {db}.{p_stg_table} 
                      where file_name in ({file_names})''' #list to str([1:-1])

insert_process_query = '''INSERT into {db}.{p_stg_table}
                        (file_name,file_location,created_date,status)
                        VALUES('{filename}','{filename}','{current_dt}','A')'''
                        
update_process_query = '''UPDATE {db}.{p_stg_table}
                        SET status='I', updated_date='{current_dt}'
                        WHERE file_name='{filename}'
                        '''