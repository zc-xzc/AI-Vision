# Third-Party and Provenance Notices

The root MIT license applies only to portions for which the repository maintainer holds the necessary rights. It does not relicense third-party examples, tutorials, model weights or datasets.

## Provenance status

| Paths / assets | Current status | Required handling |
| --- | --- | --- |
| `face_train.py`, `load_data.py` | Adapted from publicly circulated Keras face-recognition tutorial material; the original canonical source and license have not yet been conclusively identified. | Preserve this notice. Before redistributing these files outside this repository or using them commercially, identify the original source and confirm permission or replace them with an independently written implementation. |
| `UART.py`, `cmm_load.py`, embedded-camera example scripts | These files resemble board/vendor SDK examples and project adaptations. Exact upstream versions and license notices require verification. | Apply the relevant vendor/example license where identified; do not assume the root MIT license covers upstream portions. |
| `M1.tflite`, `labels_animal_fruits.txt`, `cmm_cfg.csv` | Model/data provenance is not documented in the current repository history. | The root MIT license does not grant rights to third-party model weights or datasets. Confirm ownership and training-data terms before redistribution or commercial use. |

## Contribution rule

Every newly imported file must record its source URL, author, version or commit, license and local modifications. Material without a redistribution license should not be treated as open source merely because it is publicly accessible.
