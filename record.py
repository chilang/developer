import vcr

def ignore_failed_response():
    # do not record response with status code 429 (too many requests) and 502 (bad gateway)
    def before_record_response(response):
        if response['status']['code'] in [429, 502]:
            return None
        return response
    return before_record_response

my_vcr = vcr.VCR(
    serializer='yaml',
    cassette_library_dir='recordings',
    record_mode='new_episodes',
    match_on=['uri', 'method', 'body'],
    before_record_response=ignore_failed_response(),
)