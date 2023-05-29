from ds_helper.ami_helper import ami_tag_metadata

# You need to have a valid access to AMI to run these tests!


def test_simple_tag_info_e3601():
    tag_info = ami_tag_metadata("e3601")
    assert "cacheName" in tag_info
    assert tag_info["cacheName"] == "19.2.3.3.2"


def test_simple_tag_info_p5313():
    tag_info = ami_tag_metadata("p5313")
    assert "cacheName" in tag_info
    assert tag_info["cacheName"] == "21.2.148.0"


def test_simple_tag_info_s3126():
    tag_info = ami_tag_metadata("s3126")
    assert "cacheName" in tag_info
    assert tag_info["cacheName"] == "21.0.15"


def test_simple_tag_info_r12639():
    tag_info = ami_tag_metadata("r12639")
    assert "cacheName" in tag_info
    assert tag_info["cacheName"] == "22.0.34"
