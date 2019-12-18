from typing import Hashable, Union, Tuple, Iterator, TYPE_CHECKING

from typing_extensions import Literal

TrackName = Union[str, int]
Label = Hashable
LabelGeneratorMode = Literal['int', 'string']
LabelGenerator = Union[LabelGeneratorMode, Iterator[Label]]

CropMode = Literal['intersection', 'loose', 'strict']
Alignment = Literal['center', 'loose', 'strict']
LabelStyle = Tuple[str, int, Tuple[float, float, float]]

if TYPE_CHECKING:
    from ..timeline import Timeline
    from ..annotation import Annotation
    from ..segment import Segment
    from ..feature import SlidingWindowFeature
    Key = Union[Segment, Tuple[Segment, TrackName]]
    Resource = Union[Segment, Timeline, Annotation, SlidingWindowFeature]
    Support = Union[Segment, Timeline]


