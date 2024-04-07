import sys
from hate.logger import logging
from hate.exception import HateException
from hate.configuration.gcloud_syncer import GCloudSync


obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-speech-1599","dataset.zip","dataset.zip")