import serial


class LD400P(object):
    def __init__(self, port="auto"):
        self.port = port
        self.ser = serial.Serial()

    def query(self, query, *args, response=False):
        if self.is_open():
            self.ser.write(query.format(*args))
            self.ser.flush()
            if response:
                return self.ser.readline()
            return True
        return None

    def query_response(self, query, *args):
        return self.query(query, *args, response=True)

    def get_mode(self):
        return self.query_response("MODE?")

    def set_mode(self, mode):
        return self.query("MODE {0}", mode)

    def set_cc(self):
        self.set_mode("C")

    def is_cc(self):
        return self.get_mode() == "C"

    def set_cp(self):
        self.set_mode("P")

    def is_cp(self):
        return self.get_mode() == "P"

    def set_cr(self):
        self.set_mode("R")

    def is_cr(self):
        return self.get_mode() == "R"

    def set_cg(self):
        self.set_mode("G")

    def is_cg(self):
        return self.get_mode() == "G"

    def set_cv(self):
        self.set_mode("V")

    def is_cv(self):
        return self.get_mode() == "V"

    def set_range(self, range):
        return self.query("RANGE {0}", int(range))

    def get_range(self):
        return self.query_response("RANGE?")

    def set_600W(self, on):
        return self.query("600W {0}", int(on))

    def get_600W(self):
        return self.query_response("600W?")

    def set_A(self, A):
        return self.query("A {0}", A)

    def get_A(self):
        return self.query_response("A?")

    def set_B(self, B):
        return self.query("B {0}", B)

    def get_B(self):
        return self.query_response("B?")

    def set_drop(self, drop):
        return self.query("DROP {0}", drop)

    def get_drop(self):
        return self.query_response("DROP?")

    def set_slew(self, slew):
        return self.query("SLEW {0}", slew)

    def get_slew(self):
        return self.query_response("SLEW?")

    def set_slow(self, slow):
        return self.query("SLOW {0}", slow)

    def get_slow(self):
        return self.query_response("SLOW?")

    def set_lvlsel(self, lvl):
        return self.query("LVLSEL {0}", lvl)

    def get_lvlsel(self):
        return self.query_response("LVLSEL?")

    def set_freq(self, freq):
        return self.query("FREQ {0}", freq)

    def get_freq(self):
        return self.query_response("FREQ?")

    def set_duty(self, duty):
        return self.query("DUTY {0}", duty)

    def get_duty(self):
        return self.query_response("DUTY?")

    def set_vlim(self, vlim):
        return self.query("VLIM {0}", vlim)

    def get_vlim(self):
        return self.query_response("VLIM?")

    def set_ilim(self, ilim):
        return self.query("ILIM {0}", ilim)

    def get_ilim(self):
        return self.query_response("ILIM?")

    def set_inp(self, inp):
        return self.query("INP {0}")

    def get_inp(self):
        return self.query_response("INP?")

    def get_voltage(self):
        return self.query_response("V?")

    def get_current(self):
        return self.query_response("I?")

    def get_identification(self):
        return self.query_response("*IDN?")

    def reset(self):
        return self.query("*RST")

    def save(self, save):
        return self.query("*SAV {0}", save)

    def recall(self, save):
        return self.query("*RCL {0}", save)

    def clear(self):
        return self.query("*CLS")

    def open(self):
        self.ser = serial.Serial(self.port)

    def close(self):
        self.ser.close()

    def is_open(self):
        return self.ser.is_open if self.ser is not None else False

    def __enter__(self):
        self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
