from client import AgenticDataPipelineObservabilitySchemaDriftMonitorClient

def main():
    client = AgenticDataPipelineObservabilitySchemaDriftMonitorClient()
    res = client.inspect_data_pipeline('user_signups_etl', 'analytics.users')
    print('Pipeline: ' + res['pipeline_name'] + ' | Status: ' + res['pipeline_health_status'])
    print('Freshness SLA: ' + str(res['freshness_sla_met']) + ' | Circuit Breaker: ' + str(res['auto_circuit_breaker_triggered']))
    print('Anomalies Detected:')
    for a in res['anomalies_found']:
        print('  [' + a['severity'] + '][' + a['check_type'] + '] ' + a['detail'])
        print('    Impacted Agents: ' + str(a['downstream_agents_impacted']))

if __name__ == '__main__':
    main()
