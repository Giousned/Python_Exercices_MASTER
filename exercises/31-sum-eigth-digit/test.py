import mock, pytest, io, sys 


@pytest.mark.it('The function each_digit_even must exist')
def test_function_existence(capsys, app):
    assert app.each_digit_even


@pytest.mark.it('The function should return the expected output')
def test_output(capsys, app):
    app.each_digit_even(1000,3000) == 2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,2864,2866,2868,2880,2882,2884,2886,2888

@pytest.mark.it('The solution should work with other parameters')
def test_another_entry(capsys, app):
    app.each_digit_even(3000,5000) == 4000,4002,4004,4006,4008,4020,4022,4024,4026,4028,4040,4042,4044,4046,4048,4060,4062,4064,4066,4068,4080,4082,4084,4086,4088,4200,4202,4204,4206,4208,4220,4222,4224,4226,4228,4240,4242,4244,4246,4248,4260,4262,4264,4266,4268,4280,4282,4284,4286,4288,4400,4402,4404,4406,4408,4420,4422,4424,4426,4428,4440,4442,4444,4446,4448,4460,4462,4464,4466,4468,4480,4482,4484,4486,4488,4600,4602,4604,4606,4608,4620,4622,4624,4626,4628,4640,4642,4644,4646,4648,4660,4662,4664,4666,4668,4680,4682,4684,4686,4688,4800,4802,4804,4806,4808,4820,4822,4824,4826,4828,4840,4842,4844,4846,4848,4860,4862,4864,4866,4868,4880,4882,4884,4886,4888