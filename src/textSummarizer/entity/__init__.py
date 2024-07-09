from dataclasses import dataclass
from pathlib import Path


class Pipeline:
    name: str
    #* Make sure the method is overriden
    def main(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path