from monitoring.decorators import log_exceptions, log_successes
from torrents.alcazar_client import AlcazarClient

def pause_torrent(*, torrent):
    client = AlcazarClient(timeout=AlcazarClient.TIMEOUT_LONG)
    return client.pause_torrent(torrent.realm.name, torrent.info_hash)
    
def resume_torrent(*, torrent):
    client = AlcazarClient(timeout=AlcazarClient.TIMEOUT_LONG)
    return client.resume_torrent(torrent.realm.name, torrent.info_hash)

def force_recheck(*, torrent):
    client = AlcazarClient(timeout=AlcazarClient.TIMEOUT_LONG)
    return client.force_recheck(torrent.realm.name, torrent.info_hash)

def move_data(*, torrent, download_path):
    """
    Moves entire torrent to new download path

    Notes:
    TODO Does it delete directory after copy?
    """
    client = AlcazarClient(timeout=AlcazarClient.TIMEOUT_LONG)
    return client.move_data(torrent.realm_name, 
                            torrent.info_hash, 
                            download_path)

def force_reannounce(*, torrent):
    """
    Sends Alcazard a request to recheck a torrent

    Notes:
    Respects tracker set minimum reannounce time
    """
    client = AlcazarClient(timeout=AlcazarClient.TIMEOUT_LONG)
    return client.force_reannounce(torrent.realm.name, torrent.info_hash)