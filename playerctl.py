import subprocess
import math

class PlayerctlClass:
    @staticmethod
    def check():
        try:
            cmd = "playerctl -v"
            subprocess.check_output(cmd, shell=True, text=True)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_music_status():
        cmd = "playerctl status"
        output = subprocess.check_output(cmd, shell=True, text=True)
        return output.strip()

    @staticmethod
    def get_music_play_length():
        cmd = "playerctl position"
        output = subprocess.check_output(cmd, shell=True, text=True)
        number = math.floor(float(output.strip()))
        m, s = divmod(int(math.floor(number)), 60)
        return f"{m:02d}:{s:02d}"

    @staticmethod
    def get_music_metadata():
        prepend = "\n"

        status = PlayerctlClass.get_music_status()
        playing_length = PlayerctlClass.get_music_play_length()

        if status == "Paused":
            prepend += "\n\n<color=#ff6600>Paused</color>\n"

        cmd = "playerctl metadata"
        output = subprocess.check_output(cmd, shell=True, text=True)

        data_block = output.splitlines()
        artist_entries = get_data_by_key("xesam:artist", data_block)
        track_entries = get_data_by_key("xesam:title", data_block)
        album_entries = get_data_by_key("xesam:album", data_block)

        return prepend + artist_entries + " - " + track_entries + "\n" + album_entries + "\n" + playing_length


def get_data_by_key(key, arr):
    string_data = []
    for i in arr:
        if key in i:
            value_of_key = i.split(key)[1]
            string_data.append(value_of_key.strip())
    return ", ".join(str(x) for x in string_data)
