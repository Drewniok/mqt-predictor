from mqt.predictor.devices import RigettiProvider


def test_rigetti_aspen_m2_device() -> None:
    """
    Test the import of the Rigetti Aspen-M2 quantum computer.
    """
    device = RigettiProvider.get_device("aspen-m2")
    assert device.name == "aspen-m2"
    assert device.num_qubits == 80  # noqa: PLR2004
