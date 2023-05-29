from ds_helper.ds_helpers import return_tags


def test_many_taged_ds():
    ds = "mc16_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.deriv.DAOD_PHYS.e3601_s3126_r9364_r9315_p5313"
    assert return_tags(ds) == ["e3601", "s3126", "r9364", "r9315", "p5313"]
